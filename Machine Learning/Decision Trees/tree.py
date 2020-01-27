import sys
import pandas as pd
import random
import math


class Tree:
    def __init__(self):
        self.label = ""
        self.children = []
        
    def set_label(self,newLabel):
        self.label = newLabel
        
    def add_child(self,child):
        self.children.append(child)

    def get_label(self):
        return self.label
    
    def get_children(self):
        return self.children

    def get_child_with_label(self, string):
        for child in self.children:
            if child.get_label() == string:
                return child
        return None

#helper functions
def getAttributes(data): # this returns all of the attributes for a data set to be used in ID3
    attributes = []
    for col in data.columns[1:]: #not counting the first column which is the "classification" column
        attributes.append(col)
    return attributes


def findMostCommonLabel(data): #returns the most common label out of a specific data set
    label = data.iloc[:, 0].value_counts().idxmax()
    return label


def allInstancesHaveSameLabel(data): #if all data instances have the same label it will return true, else false
    uniqueLabels = data.iloc[:,0].nunique()
    if(uniqueLabels == 1):
        return True
    else:
        return False


def entropy(s): #returns the entropy of a dataset
    size = s.shape[0] #total entries in dataset
    counts = s.iloc[:, 0].value_counts() #creates a table with the count of each possible label
    summation = 0
    if(counts.shape[0] == 1): #if there is only one data entry, return 0
        return 0
    for i in range(0,counts.shape[0]):
        summation += ((counts[i]/size) * math.log((counts[i]/size),2)) #entropy equation
    summation *= -1
    return summation


def gain(s, a): #returns the information gain of a certain attribute a 
    values = s.loc[:, a].unique() #returns all the data instances with the certain attribute a
    size = s.shape[0]
    summation = 0
    for k in range(0, len(values)):
        value = str(values[k]) 
        outcomes = s.loc[s[a] == value]

        summation += ((outcomes.shape[0] / size) * entropy(outcomes))
    return entropy(s) - summation


def findBestAttribute(a, s): #finds the attribute with the best information gain
    infoGains = [] #array of information gains that corresponds to array of attributes
    for i in range(0, len(a)): #len(A)
        infoGains.append(gain(s, a[i]))
    return a[infoGains.index(max(infoGains))]


def printTree(tree, depth): #print function to help with research questions and debugging
    print(tree.get_label())
    children = tree.get_children()
    if(len(children) == 0):
        return
    else:
        depth += 1
        for k in range(len(children)):
            for i in range(0,depth):
                print("    ",end = '')
            print("->",end='')
            printTree(children[k],depth)


def calcThreshold(s, attribute):
    # sort s based on values of attribute a
    # every time the label changes, halfway between the a values is a threshold possibility
    # calculate gain for each threshold possibility and use the one with greatest gain
    sSorted = s.sort_values(attribute)
    lastLabel = None
    thresholds = []
    lastValue = None
    for index, row in sSorted.iterrows():
        if lastLabel is not None and lastLabel != row[0]:
            threshold = 0.5 * (row[attribute] + lastValue)
            if threshold not in thresholds:
                thresholds.append(threshold)
        lastValue = row[attribute]
        lastLabel = row[0]
    #print(thresholds)

    h = entropy(s)
    gains = []
    totalRows = len(sSorted.index)
    for threshold in thresholds:
        subsetBelow = sSorted[sSorted[attribute] <= threshold]
        subsetAbove = sSorted[sSorted[attribute] > threshold]
        gain = h - ((entropy(subsetBelow) * len(subsetBelow.index) / totalRows) + (entropy(subsetAbove) * (len(subsetAbove.index) / totalRows)))
        gains.append(gain)
    max = -1
    resultIndex = -1
    for i in range(0, len(thresholds)):
        if gains[i] > max:
            max = gains[i]
            resultIndex = i
    return thresholds[resultIndex]


# end of helper functions


def createNumericBranch(subset, attributes, bestAttribute, data, numeric, below):
    branch = Tree()
    if below:
        branch.set_label("below threshold")
    else:
        branch.set_label("above threshold")
    if len(subset.index) == 0:
        leaf = Tree()
        leaf.set_label(findMostCommonLabel(subset))
        branch.add_child(leaf)
    else:
        newA = [n for n in attributes if n != bestAttribute]
        child = ID3(newA, subset, data, numeric)
        branch.add_child(child)
    return branch


def ID3(a, s, data, numeric): #creates an ID3 tree and returns the top node 
    N = Tree() #creates the head node
    if len(a) == 0: #if we have no more attributes to add to the path
        y = findMostCommonLabel(s) #use the most common label as a best guess
        N.set_label(y)
    elif allInstancesHaveSameLabel(s): #we've reached a leaf
        N.set_label(s.iloc[0, 0])  # since all labels are homogeneous we can just use the first one
    else:
        bestAttribute = findBestAttribute(a, s) #find the best attribute by checking Gain of each

        if numeric:
            threshold = calcThreshold(s, bestAttribute)
            N.set_label(bestAttribute + ":" + str(threshold))

            lowerSubset = s.loc[s[bestAttribute] <= threshold]
            upperSubset = s.loc[s[bestAttribute] > threshold]

            # create branch for values leq threshold

            if len(lowerSubset.index) > 0:
                N.add_child(createNumericBranch(lowerSubset, a, bestAttribute, data, numeric, True))
            else:
                emptyChild = Tree()
                emptyChild.set_label("below threshold")
                emptyLeaf = Tree()
                emptyLeaf.set_label(upperSubset.iloc[0, 0])
                emptyChild.add_child(emptyLeaf)
                N.add_child(emptyChild)
                # N.add_child(createNumericBranch(lowerSubset.iloc[len(lowerSubset.index) - 1], a, bestAttribute, data, numeric, True))

            # create branch for values gt threshold
            if len(upperSubset.index) > 0:
                N.add_child(createNumericBranch(upperSubset, a, bestAttribute, data, numeric, False))
            else:
                # N.add_child(createNumericBranch(upperSubset.iloc[len(upperSubset.index) - 1], a, bestAttribute, data, numeric, False))
                emptyChild = Tree()
                emptyChild.set_label("above threshold")
                emptyLeaf = Tree()
                emptyLeaf.set_label(lowerSubset.iloc[0, 0])
                emptyChild.add_child(emptyLeaf)
                N.add_child(emptyChild)
        else:
            N.set_label(bestAttribute) #create a non leaf node
            values = data.loc[:, bestAttribute].unique()
            for i in range(0, len(values)):  # for each possible value of the best attribute
                subset = s.loc[s[bestAttribute] == values[i]] #partition the instances into Sv subsets
                if subset.shape[0] == 0:  #this attribute value is not present in S
                    branch = Tree()
                    branch.set_label(values[i])  # set the branch's label to the current VALUE for best attribute
                    leaf = Tree()  # create a leaf node with our best guess of the label
                    leaf.set_label(findMostCommonLabel(s))  # set the leaf's label to the most common LABEL in s
                    branch.add_child(leaf)
                    N.add_child(branch)
                else:
                    branch = Tree() #recursively grow children
                    branch.set_label(values[i])
                    newA = [n for n in a if n != bestAttribute]
                    child = ID3(newA, subset, data, numeric)
                    branch.add_child(child)
                    N.add_child(branch)
    return N


def splitTrainingTesting(df,train,seed): #same implementation as previous assignments
    size = df.shape[0]
    indexList = list(range(size))
    trainingLimit = round(train*size)
    random.seed(seed)
    random.shuffle(indexList)
    training = pd.DataFrame(columns = df.columns)
    test = pd.DataFrame(columns = df.columns)
    for i in range(0,trainingLimit):
        trainIndex = indexList[i]
        training.loc[i] = df.iloc[trainIndex]
    indexList = indexList[trainingLimit:]
    testLimit = size - trainingLimit
    for k in range(0,testLimit):
        testIndex = indexList[k]
        test.loc[k]=df.iloc[testIndex]
    return training,test


def testTree(tree, testSet, possibleLabels, numeric):
    matrix = [[0 for x in range(len(possibleLabels))] for y in range(len(possibleLabels))]
    for index, row in testSet.iterrows():
        node = tree
        while len(node.get_children()) > 0:  # while we're not at a leaf
            if numeric:
                treeLabelArr = node.get_label().split(':')
                if row[treeLabelArr[0]] <= float(treeLabelArr[1]):
                    node = node.get_child_with_label("below threshold").get_children()[0]
                else:
                    node = node.get_child_with_label("above threshold").get_children()[0]
            else:
                treeLabel = node.get_label()
                #print("tree label:" ,treeLabel)
                children = node.get_children()
                for i in range(0,len(children)):
                    #print("child label: ",children[i].get_label())
                    #print("test label: ",row[treeLabel])
                    if(children[i].get_label() == row[treeLabel]):
                        node = children[i].get_children()[0]
                        #print(node.get_label())
                        break
                #testLabel = row[treeLabel]
                #print("test label:",testLabel)
        if len(node.get_children()) == 0:  # we're at a leaf
            prediction = node.get_label()
            # increment the box in matrix of column equal to predicted and row equal to actual
            actual = row[0]
            matrix[possibleLabels.index(actual)][possibleLabels.index(prediction)] += 1

    file = open("results_tree_" + sys.argv[1][:-4] + "_" + str(numeric) + "_" + sys.argv[2] + "_" + sys.argv[3] + ".csv", "w+")
    for label in possibleLabels:
        file.write(str(label) + ",")
        #print(str(label) + ",", end="")
    #print()
    file.write("\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            file.write(str(matrix[i][j]) + ",")
            #print(str(matrix[i][j]) + ",", end="")
        #print(possibleLabels[i])
        file.write(str(possibleLabels[i]))
        file.write("\n")
    file.close()


def main():
    fileData = pd.read_csv(sys.argv[1])
    trainingPercent = float(sys.argv[2])
    seed = int(sys.argv[3])
    numeric = str(sys.argv[4])
    if numeric.lower() == "true":
        numeric = True
    else:
        numeric = False
    #print("Parsing file:", sys.argv[1])
    training,test = splitTrainingTesting(fileData, trainingPercent, seed)
    attributes = getAttributes(training)
    #print("Done parsing.")
    tree = ID3(attributes, training, fileData, numeric)
    #printTree(tree, 0)
    possibleLabels = list(fileData.iloc[:, 0].unique())
    testTree(tree, test, possibleLabels, numeric)
        


if __name__ == '__main__':
    main()
#monks should be above 90 percent, should be less than a second
#opticaldigit should be 50 percent and should take around 2 seconds for no numbers, 25 for numbers 88percent accuracy
#when you call node.children["sunny"] = learn(Ssunny, A)
    #right before you make a recursive call with A, make a new list... newA = list(A)
    #count right number of thresholds
