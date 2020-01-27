def euclidian(testElement,training): #euclidian distance algorithm
    import math 
    distances = []
    for trainingElement in training: #loops through all the training elements
        dist = 0
        for m in range(1,len(testElement)): #loops through each attribute
            difference = testElement[m] - trainingElement[m] #finds the difference in distance
            dist += (difference * difference)   #squares the distance
        dist = math.sqrt(dist) #square roots the sum of distances
        distances.append(dist) 
    return distances

def hamming(testElement,training): #hamming distance algorithm
    distances = []
    for trainingElement in training: #loops through training 
        dist = 0
        for m in range(1,len(testElement)): #loops through each attribute
            if testElement[m] != trainingElement[m]: #if the attribute is different, it adds 1 to distance
                dist +=1
        distances.append(dist)
    return distances

def most_frequent(List): #this function is here to find the most common element in the list of neighbors for n neighbors
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num

def calculateAccuracy(training,test,distFunc,k): #does most of the work of the program
    predicted = []
    actual = []
    labels= []
    for testElement in test: #loops through all test elements
        if(distFunc == "E"): #euclidian 
            distances = euclidian(testElement,training)
        else: #hamming
            distances = hamming(testElement,training)
        minDistance = [] 
        #loops through the distances and finds the smalllest distances 
        for i in range(0,len(distances)):
            if i < k:
                minDistance.append(distances[i])
            else:
                if distances[i] < max(minDistance):
                    minDistance[minDistance.index(max(minDistance))] = distances[i]
        
        predictionIndices = []
        #finds the indices of the minDistances in the distances list
        for i in range(0, len(minDistance)):
            predictionIndices.append(distances.index(minDistance[i]))
        predictions = []
        #goes through each predictionIndex and finds the correlating classification in the training list
        for m in predictionIndices:
            predictions.append(training[m][0])
        predicted.append(most_frequent(predictions))
    for i in test: #this loop gives the list of possible labels 
        actual.append(i[0])
        if len(labels) == 0:
            labels.append(i[0])
        elif i[0] in labels:
            continue
        else:
            labels.append(i[0])
    matrix = []
    for m in range(0,len(labels)): #these two loops create the matrix necessary for printing
        matrixEntry = [0] * (len(labels) + 1)
        matrixEntry[0] = labels[m]
        matrix.append(matrixEntry)
    for p in range(0,len(predicted)):
        predictedIndex = labels.index(predicted[p])
        actualIndex = labels.index(actual[p]) + 1
        matrix[predictedIndex][actualIndex] += 1
    return labels,matrix
                
            
def createTrainingSet(seed,percentage,entireList): #creates the training set and test set
    import random
    trainingLimit = round(percentage * len(entireList)) #finds the necessary number of instances for each set
    sizeOfEntireList = len(entireList) - 1
    trainingSet = []
    random.seed(seed) #uses the seed necessary for randomization 
    for i in range(0,trainingLimit): 
        index = random.randint(0,sizeOfEntireList) #finds a random index to put in the training set
        trainingSet.append(entireList[index])
        del entireList[index]
        sizeOfEntireList -= 1
    return trainingSet,entireList

#parseFile
def parseFile(file,nominal): #parses the file into a list
    counter = 0
    data = []
    for line in file:
        if counter==0 or nominal:
            startline = line.strip().split(",")
            startlineStrings = []
            for i in startline:
                startlineStrings.append(str(i).replace('"',''))
            data.append(startlineStrings)
        else:
            dataLine = line.strip().split(",")
            dataValues = []
            dataValues.append(str(dataLine[0].replace('"','')))
            for x in range(1,len(dataLine)):
                dataValues.append(float(dataLine[x]))
            data.append(dataValues)
        counter +=1
    return data

#main
import sys
filePath = open(sys.argv[1])
distFunc = str(sys.argv[2])
k = int(sys.argv[3])
trainingPercent = float(sys.argv[4])
seed = int(sys.argv[5])
nominal = False
if(str(sys.argv[1]) == "monks1.csv"): #case statement here for monks (for parsing purposes)
    nominal = True
wholeSet = parseFile(filePath,nominal)
training,test = createTrainingSet(seed, trainingPercent,wholeSet[1:])
labels,matrix = calculateAccuracy(training,test,distFunc,k)
for L in labels:
    print(L + ",",end ='')
print()
for i in range(1,len(matrix)+1):
    for m in matrix:
        print(str(m[i])+",",end='')
    print(labels[i-1])

