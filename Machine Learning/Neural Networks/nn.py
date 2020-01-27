import sys
import pandas as pd
import numpy as np
import random
import math
import csv

def sigmoid(x): #applies the sigmoid function
    return 1 / (1 + math.exp(-x))

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) 


class Neuron:
    def __init__(self, attribute_count, outputNeuron):
        self.weights = []
        self.wZero = random.uniform(-.1, .1)
        self.outputNeuron = outputNeuron 
        for i in range(0, attribute_count):
            self.weights.append(random.uniform(-.1, .1))

    # instances: the set of instances
    # row: index in instances of the row we want to feed into this neuron
    def activation(self, instances, row):
        result = self.wZero
        for i in range(1, len(instances.columns)):  # starting at 1 because we don't want to include the label
            result += self.weights[i-1]*instances.iat[row, i]  # weights are 0-based but we're starting at attribute 1,
            # so we subtract 1 from our index in the columns to get the correct weight
        return sigmoid(result)

    # generates the activation of the output neuron
    # inputs: list of activations from the hidden layer
    def output_activation(self, inputs):
        result = 0
        #print("weights",self.weights,"\ninputs",inputs,"\nwZero",self.wZero)
        for i in range(0, len(self.weights)):
            result += self.weights[i]*inputs[i]
        #print("output result before sigmoid",result)
        result += self.wZero
        return sigmoid(result)

    def get_weights(self):
        return self.weights

    def get_bias(self):
        return self.wZero

    def set_weight(self, index, value):
        self.weights[index] = value

    def set_bias(self, value):
        self.wZero = value
        
def testActivation(weights,inputs,wZero):
    result = 0 
    for i in range(0,len(weights)):
        result += weights[i]*inputs[i]
    result += wZero
    return(sigmoid(result))

def createNeuralNetwork(training,totalNeurons):
    hiddenLayer =[]
    numberOfAttributes = training.shape[1]-1
    outputNeuron = Neuron(totalNeurons,None) 
    for i in range(0,totalNeurons):
        hiddenLayer.append(Neuron(numberOfAttributes,outputNeuron))
    return hiddenLayer


def backpropagation(hidden, training, validation, learning_rate, threshold):
    accuracy = 0
    epochs = 0
    output_neuron = hidden[0].outputNeuron

    while accuracy < 0.99 and epochs < 1:  # TODO && accuracy on validation set hasn't gotten worse
        #print("output neuron bias", output_neuron.get_bias())
        #print("output neuron weights",output_neuron.get_weights())
        activations = []
        feedbacks = []
        for i in range(0, 1):  # for each training instance len(training)
            #print(training.loc[i,:])
            feedbacks.clear()
            activations.clear()
            
            for neuron in hidden:  # calculate activations for each hidden neuron
                activations.append(neuron.activation(training, i))
            
            #print("hidden neuron activations",activations)
            #firstActivation = output_neuron.output_activation(activations)
            #secondActivation = testActivation(output_neuron.get_weights(),activations,output_neuron.get_bias())
            #print("firstActivation",firstActivation)
            #print("secondActivation",secondActivation)
            result = testActivation(output_neuron.get_weights(),activations,output_neuron.get_bias())  #output_neuron.output_activation(activations)# calculate activation for output neuron
            #print("output neuron activation", result)
            #print("actual",training.iat[i,0])
            activation_prime = result * (1 - result)
            # calculate output feedback. output feedback = activation' * error
            # error = training.iat[i, 0] - result
            output_feedback = activation_prime * (training.iat[i, 0] - result)
            #print("output_feedback",output_feedback)
            # calculate feedback for each neuron in the hidden layer
            for j in range(0, len(hidden)):
                # feedback = activation' * weight in output neuron corresponding to this hidden neuron * output feedback
                hidden_activation_prime = activations[j] * (1 - activations[j])
                feedbacks.append(hidden_activation_prime * output_neuron.get_weights()[j] * output_feedback)
            #print("feedbacks hid",feedbacks)
            # end loop through each hidden neuron

            # update bias for output neuron
            
            output_neuron.set_bias(output_neuron.get_bias() - (-learning_rate * output_feedback))

            for k in range(0, len(output_neuron.get_weights())):  # update weights for output neuron
                
                output_neuron.set_weight(k, output_neuron.get_weights()[k] 
                                         - (-learning_rate * output_feedback * activations[k]))
                
                

            # update the weights for each hidden neuron
            for j in range(0, len(hidden)): #len(hidden)
                # update w0
                hidden[j].set_bias(hidden[j].get_bias() - (-learning_rate * feedbacks[j]))
                #print("hidden weights for first hidden neuron", hidden[j].get_weights())
                for k in range(0, len(hidden[j].get_weights())):  # for each weight in this hidden neuron
                    # in training set 0th attribute is the label so we add 1 to the index of its weight to get its value
                    # i = which training instance we're on, k = which weight we're on
                    print("old weight:",hidden[j].get_weights()[k])
                    print("actual: ",training.iat[i,0])
                    print("attribute value",training.iat[i, k + 1])
                    print("predicted: ",result)
                    print("weight change: ",(-learning_rate * feedbacks[j] * training.iat[i, k + 1]))
                    weight_update = -learning_rate * feedbacks[j] * training.iat[i, k + 1]
                    hidden[j].set_weight(k, hidden[j].get_weights()[k] - weight_update)    
                    print("new weight: ",hidden[j].get_weights()[k])
                #print("hidden weights for first hidden neuron", hidden[j].get_weights())
            
                    # print("updated weight:", hidden[j].get_weights()[k])
                # end loop through weights in this hidden neuron
            # end loop through each hidden neuron
        # end loop through training set

        predictions = []
        decimal_predictions = []
        correct = 0
        incorrect = 0
        #print("output_neuron bias",output_neuron.get_bias())
        #print("output_neuron weights",output_neuron.get_weights())
        for i in range(0, len(validation)): #len(validation)
            validation_activations = []
            
            for neuron in hidden:  # calculate activations for each hidden neuron
                validation_activations.append(neuron.activation(validation, i))
            
            y_hat = testActivation(output_neuron.get_weights(),validation_activations,output_neuron.get_bias())  # calculate activation for output neuron
            #if(i == 9):
                #print("validation output neuron activation",y_hat)
                #print("validation output neuron weights",output_neuron.get_weights())
                #print("wZero", output_neuron.get_bias())
            decimal_predictions.append(y_hat)
            if y_hat < threshold:
                y_hat = 0
            else:
                y_hat = 1
            actual = validation.iat[i, 0]
            
            if(y_hat == actual):
                correct += 1
            else:
                incorrect += 1
            predictions.append(y_hat)
            #if(i ==9):
                #print("validation hidden neuron activations",validation_activations)
                
                #print("actual: ",actual)
                #print("test activation: ",testActivation(output_neuron.get_weights(),validation_activations,output_neuron.get_bias()))
        # end loop through validation set

        validationPercentCorrect = correct / (correct + incorrect)
        print("percent correct:", validationPercentCorrect)

        # print("length of validation set:", len(validation))
        print("predictions for validation set:", predictions)
        #print("output neuron bias", output_neuron.get_bias())
        #print("output neuron weights",output_neuron.get_weights())
        #print("decimal predictions for validation set:", decimal_predictions)
        #print("w0 for first hidden neuron:", hidden[0].wZero)
        epochs += 1
    # end while loop

def dataPreProcessing(df,train,seed): #data preprocessing that scales values and provides one hot encoding
    import random
    for column in df.columns: #this loop gives the one-hot-encoding for converting the nominal attributes into boolean values. One category is always dropped
        if(df[column].dtype == 'object'):
            df = pd.concat([df,pd.get_dummies(df[column],prefix=column,drop_first=True)],axis=1)
            df.drop([column],axis=1,inplace=True)
        elif(df[column].dtype == 'int64' or df[column].dtype == 'float64'): #for scaling
            max_value = df[column].max()
            min_value = df[column].min()
            if max_value == 0: #some values (especially in seismic) 0 values throughout the entire column
                continue
            else:
                df[column] = df[column].apply(lambda x: (x-min_value)/(max_value-min_value)) #applies the new scaling to entire column
        
    size = df.shape[0] # after scaling and encoding we now separate into different sets
    indexList = list(range(size))
    trainingLimit= round(train * size)
    valid = (1 - train)/2 #percentage of dataset to be used for validation set (and test set)
    validLimit = round(valid * size)
    random.seed(seed)
    random.shuffle(indexList) #the size of the entire set is put into a list and shuffled so indices can be found in the main set and
                              #placed into the other sets
    training = pd.DataFrame(columns = df.columns) #uses the panda dataframe
    validation = pd.DataFrame(columns = df.columns)
    test = pd.DataFrame(columns = df.columns)
    for i in range(0,trainingLimit):
        trainIndex = indexList[i]
        training.loc[i] = df.iloc[trainIndex] #moving the variable from the main dataset over to training
    indexList = indexList[trainingLimit:] #updates the indexList for the validation set
    for k in range(0,validLimit):
        validIndex = indexList[k]
        validation.loc[k] = df.iloc[validIndex]
    indexList = indexList[validLimit:]
    testLimit = size - trainingLimit - validLimit
    for j in range(0,testLimit):
        validIndex = indexList[j]
        test.loc[j] = df.iloc[validIndex]
    return training,validation,test


def main():
    df = pd.read_csv(sys.argv[1]) #df is dataFrame. This automatically puts all the data into a panda dataframe
    neurons = int(sys.argv[2]) #number of neurons to use in hidden layer
    learningRate = float(sys.argv[3])
    trainingPercent = float(sys.argv[4])
    seed = int(sys.argv[5])
    threshold = float(sys.argv[6])
    training,validation,test = dataPreProcessing(df,trainingPercent,seed)
    hiddenLayer = createNeuralNetwork(training,neurons)
    backpropagation(hiddenLayer, training, validation, learningRate,threshold)
    # print(training)


if __name__ == '__main__':
    main()
