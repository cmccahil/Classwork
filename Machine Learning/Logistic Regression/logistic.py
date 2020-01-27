import math
import random
import csv

def testWeights(test,wZero,weights): #this runs through the test set and uses the algorithm to make predictions
    correct = 0
    incorrect = 0
    yesYes =0
    noNo=0
    noYes=0
    yesNo=0
    for i in range(0,test.shape[0]):
        summationOfWeights = 0
        for j in range(1,len(weights)):
            summationOfWeights += (test.iat[i,j]*weights[j]) #summing up weights
        predictionPercent = wZero + summationOfWeights #applying wZero
        prediction = sigmoid(predictionPercent) #applying sigmoid function
        if(prediction >= .5): #making prediction
            prediction = 1
        else:
            prediction = 0
        actual = test.iat[i,0] #getting actual answer for the row
        if(prediction == actual): #adding to output
            correct +=1
            if(actual == 1):
                yesYes += 1
            else:
                noNo +=1
        else:
            incorrect +=1
            if(actual == 1):
                noYes += 1
            else:
                yesNo += 1
    validationPercentCorrect = correct / (correct + incorrect) #for Readme questions
    #print("Percent of Test correct")
    #print(validationPercentCorrect)
    #print("Yes,No,")
    #print(yesYes,noYes,'Yes')
    #print(yesNo,noNo,'No')
    #print("TotalValues: ",correct+incorrect)
    return yesYes,noNo,yesNo,noYes,validationPercentCorrect

def sigmoid(x): #applies the sigmoid function
    return 1 / (1 + math.exp(-x))

def calculateWeights(training,validation,rate,seed):
    random.seed(seed)
    totalWeights = training.shape[1]
    wZero = random.uniform(-.1,.1) #choosing random value for w0
    weights = []
    lengthOfTrainingSet = training.shape[0]
    lengthOfValidation = validation.shape[0]
    for i in range(0,totalWeights): #choosing random weights for wI
        weights.append(random.uniform(-.1,.1))
    epochs = 0
    validationPercentCorrect = 0.0 #for README questions
    validationAccuracyModel = [] #""
    while(validationPercentCorrect < .99 and epochs < 500): #here begins the algorithm
        for j in range(0, lengthOfTrainingSet):
            summationOfWeights = 0.0 
            for i in range(1,totalWeights): #we start at 1, because the first column is the prediction
                summationOfWeights += (training.iat[j,i]*weights[i])
            predictionNet = wZero + summationOfWeights
            prediction = sigmoid(predictionNet)
            actual = training.iat[j,0]
            changeWZero=-1.0*prediction*(1.0-prediction)*(actual-prediction)
            changeWeights = [0] 
            for k in range(1,len(weights)):
                changeWeights.append((-training.iat[j,k])*prediction*(1.0-prediction)*(actual-prediction))
            wZero = wZero - (rate * changeWZero)
            for m in range(1,len(weights)):
                weights[m] = weights[m] - (rate * changeWeights[m]) 
        correct = 0
        incorrect = 0
        for i in range(0,lengthOfValidation): #loop through validation set to test new weights from training
            summationOfWeights = 0
            for j in range(1,len(weights)):
                summationOfWeights += (validation.iat[i,j]*weights[j])
            predictionPercent = wZero + summationOfWeights
            prediction = sigmoid(predictionPercent)
            if(prediction >= .5):
                prediction = 1
            else:
                prediction = 0
            actual = validation.iat[i,0]
            if(prediction == actual):
                correct +=1
            else:
                incorrect +=1
        validationPercentCorrect = correct / (correct + incorrect)
        validationAccuracyModel.append(validationPercentCorrect) #for README
        epochs += 1
    #print(validationAccuracyModel)
    return wZero,weights    

def dataPreProcessing(df,train,valid,seed): #data preprocessing that scales values and provides one hot encoding
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
        
    size = df.shape[0] #after scaling and encoding we now separate into different sets
    indexList = list(range(size))
    trainingLimit= round(train * size)
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

def writeCSV(DataSet,LearningRate,seed,yesYes,noNo,yesNo,noYes): #writes the output to the csv file
    fileName = "results_"+DataSet+"_"+LearningRate+"r_"+seed+".csv"
    with open(fileName,mode='w') as output_file:
        output_writer = csv.writer(output_file,quotechar='"',quoting=csv.QUOTE_MINIMAL)
        output_writer.writerow(['Yes','No'])
        output_writer.writerow([yesYes,noYes,'Yes'])
        output_writer.writerow([yesNo,noNo,'No'])
    #print(fileName)

#main
import sys
import pandas as pd
import numpy as np
df = pd.read_csv(sys.argv[1]) #df is dataFrame. This automatically puts all the data into a panda dataframe
learningRate = float(sys.argv[2])
trainingPercent = float(sys.argv[3])
validPercent = float(sys.argv[4])
seed = int(sys.argv[5])
training,validation,test = dataPreProcessing(df,trainingPercent,validPercent,seed)
wZero,weights = calculateWeights(training,validation,learningRate,seed)
yesYes,noNo,yesNo,noYes,percentCorrect = testWeights(test,wZero,weights)
writeCSV(str(sys.argv[1])[:-4],str(learningRate),str(seed),yesYes,noNo,yesNo,noYes)
#print(percentsCorrect) #these are for the REAMDE
#total = 0
#outsideConfidenceInterval = 0
#for percent in percentsCorrect:
#    total += percent
#    if (percent > 0.9923 or percent <0.9859):
#        outsideConfidenceInterval +=1
#print(total /30)
#print(outsideConfidenceInterval)
