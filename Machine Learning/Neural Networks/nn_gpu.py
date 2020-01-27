import data_reader
import confusion_matrix
import random
import sys
import tensorflow as tf
import time

def runNetwork(train, valid, test, neurons, learningRate, threshold, numAttributes, possibleLabels):
    numLabels = len(possibleLabels)
    if numLabels == 2:
        numLabels = 1 # binary classification uses a single variable that is 0 or 1

    # move the data to GPU memory
    trainX = tf.constant(train[0])
    trainY = tf.constant(train[1])
    validX = tf.constant(valid[0])
    #validY = tf.constant(test[1])
    testX = tf.constant(test[0])
    #testY = tf.constant(test[1])

    # first, construct the neural network

    # create the hidden layer
    W_hidden = tf.Variable(tf.random_uniform([numAttributes, neurons], minval=-0.1, maxval=0.1))
    b_hidden = tf.Variable(tf.random_uniform([neurons], minval=-0.1, maxval=0.1))

    # create the calculations in the hidden layer
    hidden_net_train = tf.matmul(trainX, W_hidden) + b_hidden
    hidden_out_train = tf.sigmoid(hidden_net_train)

    hidden_net_valid = tf.matmul(validX, W_hidden) + b_hidden
    hidden_out_valid = tf.sigmoid(hidden_net_valid)

    hidden_net_test = tf.matmul(testX, W_hidden) + b_hidden
    hidden_out_test = tf.sigmoid(hidden_net_test)

    # create the output layer
    W_outlayer = tf.Variable(tf.random_uniform([neurons, numLabels], minval=-0.1, maxval=0.1))
    b_outlayer = tf.Variable(tf.random_uniform([numLabels], minval=-0.1, maxval=0.1))

    # create the calculations in the output layer
    output_net_train = tf.matmul(hidden_out_train, W_outlayer) + b_outlayer
    output_net_valid = tf.matmul(hidden_out_valid, W_outlayer) + b_outlayer
    output_net_test = tf.matmul(hidden_out_test, W_outlayer) + b_outlayer

    if numLabels == 1:
        yhat_train = tf.sigmoid(output_net_train)
        yhat_valid = tf.sigmoid(output_net_valid)
        yhat_test = tf.sigmoid(output_net_test)
    else:
        yhat_train = tf.nn.softmax(output_net_train)
        yhat_valid = tf.nn.softmax(output_net_valid)
        yhat_test = tf.nn.softmax(output_net_test)

    # setup training
    if numLabels == 1:
        cost = tf.reduce_sum(0.5 * (trainY - yhat_train) * (trainY - yhat_train))
    else:
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=trainY, logits=output_net_train))
    trainStep = tf.train.AdamOptimizer(learningRate).minimize(cost)

    # start the session
    sess = tf.Session()
    init = tf.initialize_all_variables().run(session=sess)

    # setup the params
    epoch = 0
    printEvery = 50
    maxEpochs  = 500
    totalTime = 0
    validAcc = 0.0

    while epoch < maxEpochs and validAcc < 0.99:
        epoch += 1

        # train the network
        startTime = time.process_time()
        sess.run(trainStep)
        totalTime += time.process_time() - startTime

        if epoch % printEvery == 0:
            p = sess.run(yhat_train)

            print("\n###################################################")
            print("\nEpoch:", epoch, "\tTime:", totalTime / epoch)

            print("Training:")
            cm = confusion_matrix.buildConfusionMatrix(p, train[1], numLabels, threshold)
            confusion_matrix.printConfusionMatrix(cm, possibleLabels)
            confusion_matrix.printAccuracy(cm)

            print("\nValidation:")
            p = sess.run(yhat_valid)
            print(len(p), len(valid[1]))
            cm = confusion_matrix.buildConfusionMatrix(p, valid[1], numLabels, threshold)
            confusion_matrix.printConfusionMatrix(cm, possibleLabels)
            confusion_matrix.printAccuracy(cm)

    # evaluate the test accuracy
    p = sess.run(yhat_test)

    print("\n***************************************************")
    print("\nConfusion Matrix on Test Set:")
    cm = confusion_matrix.buildConfusionMatrix(p, test[1], numLabels, threshold)
    confusion_matrix.printConfusionMatrix(cm, possibleLabels)
    confusion_matrix.printAccuracy(cm)
    print("Average time:", totalTime / epoch)


def main():
    # get the parameters
    datafile = sys.argv[1]
    neurons = int(sys.argv[2])
    learningRate = float(sys.argv[3])
    threshold = float(sys.argv[4])
    trainPerc = float(sys.argv[5])
    seed = int(sys.argv[6])

    # set up the RNG
    random.seed(seed)

    # read in the data
    reader = data_reader.DataReader(datafile, trainPerc)
    numAttributes, numLabels = reader.readData()
    possibleLabels = reader.discreteValues[data_reader.DataReader.LABEL_COLUMN]

    # get the randomized training and test sets
    train, valid, test = reader.splitData()

    # train the network
    runNetwork(train, valid, test, neurons, learningRate, threshold, numAttributes, possibleLabels)


if __name__ == "__main__":
    main()