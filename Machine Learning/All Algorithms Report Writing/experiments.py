import sys
import pandas as pd
import numpy as np
import csv
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB

def preProcessing(df,seed): #preprocessing necessary for the dataSet in order to feed into the algorithms
    for column in df.columns[1:]: #one hot encoding (does not one hot encode the label)
        if(df[column].dtype == 'object'):
            df = pd.concat([df,pd.get_dummies(df[column],prefix=column,drop_first=True)],axis=1)
            df.drop([column],axis=1,inplace=True)
    size = df.shape[0]
    indexList = list(range(size))
    trainingLimit = round(.75 * size) #training percent will be 75%
    testLimit = size - trainingLimit
    random.seed(seed)
    random.shuffle(indexList)
    training = pd.DataFrame(columns = df.columns)
    test = pd.DataFrame(columns = df.columns)
    for i in range(0,trainingLimit): #fills in the training set
        training.loc[i] = df.iloc[indexList[i]]
    indexList = indexList[trainingLimit:]
    for i in range(testLimit): #fills in the test set
        test.loc[i] = df.iloc[indexList[i]]
    #print(training)
    return training,test

def matrix(actual,predicted,labels,approach,dataSet): #takes results from algorithms and creates a csv file matrix
    matrix = []
    for m in range(len(labels)): #creating the template for the matrix
        matrixEntry = [0] * (len(labels)+1)
        matrixEntry[0] = labels[m]
        matrix.append(matrixEntry)
    for p in range(len(predicted)): #filling in the values for the matrix
        predictedIndex = np.where(labels == predicted[p])[0][0]
        actualIndex = np.where(labels == actual[p])[0][0] + 1
        matrix[predictedIndex][actualIndex] += 1
    fileName = "results_"+approach+"_"+dataSet #creates a csv file with the results of the matrix
    file = open(fileName,"w+")
    for i in range(len(matrix)):
        file.write(matrix[i][0]+",")
    file.write("\n")
    for j in range(1,len(matrix)+1):
        for k in range(len(matrix)):
            file.write(str(matrix[k][j])+",")
        file.write(matrix[j-1][0]+"\n")

def main():
    dataSets = ["monks1.csv","votes.csv","hypothyroid.csv","mnist_1000.csv"]
    seed = int(sys.argv[1])
    for i in range(0,len(dataSets)):#len(dataSets)
        df = pd.read_csv(dataSets[i])
        training,test = preProcessing(df,seed)
        
        #in order to feed data into the sklearn algorithms, we need to split into y(the labels) and x(the data that determines the labels)
        x_train = training.drop(training.columns[0],axis = 1)  
        y_train = training[training.columns[0]]
        x_test = test.drop(test.columns[0],axis=1)
        y_test = test[test.columns[0]]
        labels = df[df.columns[0]].unique()
        
        #Decision Tree
        classifier = DecisionTreeClassifier()
        classifier.fit(x_train,y_train)
        y_pred = classifier.predict(x_test)
        approach = "DecisionTree"
        matrix(y_test,y_pred,labels,approach,dataSets[i])
        
        #Neural Network
        #3 hidden layers with 10 hidden units each 
        mlp = MLPClassifier(hidden_layer_sizes=(10,10,10),max_iter=1000)
        mlp.fit(x_train,y_train)
        y_pred = mlp.predict(x_test)
        approach = "NeuralNetworks"
        matrix(y_test,y_pred,labels,approach,dataSets[i])

        #Naive Bayes
        model = MultinomialNB().fit(x_train,y_train)
        y_pred = model.predict(x_test)
        approach = "NaiveBayes"
        matrix(y_test,y_pred,labels,approach,dataSets[i])
        

if __name__ == '__main__':
    main()
