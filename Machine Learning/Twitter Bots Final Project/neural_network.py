import data_reader
import confusion_matrix
import random
import sys
import time
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


def runNetwork(train, valid, test, neurons, learningRate, threshold, numAttributes, possibleLabels, outputFile):
    numLabels = len(possibleLabels)
    if numLabels == 2:
        numLabels = 1 # binary classification uses a single variable that is 0 or 1

    # first, construct the neural network

    # build the input layer
    x = tf.placeholder(tf.float32, shape=[None, numAttributes])

    # build the placeholder for the true labels
    y = tf.placeholder(tf.float32, shape=[None, numLabels])

    # create the hidden layer
    W_hidden = tf.Variable(tf.random_uniform([numAttributes, neurons], minval=-0.1, maxval=0.1))
    b_hidden = tf.Variable(tf.random_uniform([neurons], minval=-0.1, maxval=0.1))

    #W_hidden = tf.Variable(tf.zeros([numAttributes, NUM_NEURONS]))
    #b_hidden = tf.Variable(tf.constant(0.0, shape=[NUM_NEURONS]))

    # create the calculations in the hidden layer
    hidden_net = tf.matmul(x, W_hidden) + b_hidden
    hidden_out = tf.sigmoid(hidden_net)

    # create the output layer
    W_outlayer = tf.Variable(tf.random_uniform([neurons, numLabels], minval=-0.1, maxval=0.1))
    b_outlayer = tf.Variable(tf.random_uniform([numLabels], minval=-0.1, maxval=0.1))

    #W_outlayer = tf.Variable(tf.zeros([NUM_NEURONS, numLabels]))
    #b_outlayer = tf.Variable(tf.constant(0.0, shape=[numLabels]))

    # create the calculations in the output layer
    output_net = tf.matmul(hidden_out, W_outlayer) + b_outlayer

    if numLabels == 1:
        yhat = tf.sigmoid(output_net)
    else:
        yhat = tf.nn.softmax(output_net)

    # setup training
    if numLabels == 1:
        cost = tf.reduce_sum(0.5 * (y - yhat) * (y - yhat))
    else:
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=output_net))
    trainStep = tf.train.AdamOptimizer(learningRate).minimize(cost)

    # start the session
    sess = tf.Session()
    init = tf.initialize_all_variables().run(session=sess)

    # setup the params
    epoch = 0
    printEvery = 1
    maxEpochs = 500
    totalTime = 0
    validAcc = 0.0

    while epoch < maxEpochs and validAcc < 0.99:
        epoch += 1

        # train the network
        startTime = time.process_time()
        sess.run(trainStep, feed_dict={x: train[0], y: train[1]})
        totalTime += time.process_time() - startTime

        if epoch % printEvery == 0:
            p = sess.run(yhat, feed_dict={x: train[0]})

            print("\n###################################################")
            print("\nEpoch:", epoch, "\tTime:", totalTime / epoch)

            print("Training:")
            cm = confusion_matrix.buildConfusionMatrix(p, train[1], numLabels, threshold)
            confusion_matrix.printConfusionMatrix(cm, possibleLabels, None)
            confusion_matrix.printAccuracy(cm, None)

            print("\nValidation:")
            p = sess.run(yhat, feed_dict={x: valid[0]})
            cm = confusion_matrix.buildConfusionMatrix(p, valid[1], numLabels, threshold)
            confusion_matrix.printConfusionMatrix(cm, possibleLabels, None)
            confusion_matrix.printAccuracy(cm, outputFile)

    # evaluate the test accuracy
    p = sess.run(yhat, feed_dict={x: test[0]})

    print("\n***************************************************")
    print("\nConfusion Matrix on Test Set:")
    cm = confusion_matrix.buildConfusionMatrix(p, test[1], numLabels, threshold)
    confusion_matrix.printConfusionMatrix(cm, possibleLabels, outputFile)
    confusion_matrix.printAccuracy(cm, outputFile)
    print("Average time:", totalTime / epoch)


def main():
    # get the parameters
    datafile = sys.argv[1]
    neurons = int(sys.argv[2])
    learningRate = float(sys.argv[3])
    threshold = float(sys.argv[4])
    trainPerc = float(sys.argv[5])
    seed = int(sys.argv[6])
    title = sys.argv[7]

    # set up the RNG
    random.seed(seed)
    outputFile = open("results_nn_" + title + "_" + sys.argv[2] + "_" + sys.argv[3] + "_" + sys.argv[4] + "_" + sys.argv[5] + "_" + sys.argv[6] + ".txt", "w")

    # read in the data, we edited parts of this to get rid of columns that were irrelevant
    reader = data_reader.DataReader(datafile, trainPerc, outputFile)
    numAttributes, numLabels = reader.readData()
    possibleLabels = reader.discreteValues[data_reader.DataReader.LABEL_COLUMN]

    # get the randomized training and test sets
    train, valid, test = reader.splitData()

    # train the network
    runNetwork(train, valid, test, neurons, learningRate, threshold, numAttributes, possibleLabels, outputFile)

    outputFile.close()


if __name__ == "__main__":
    main()
