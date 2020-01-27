import csv
import random


class DataReader:
    # the column of the label
    LABEL_COLUMN = 0

    def __init__(self, datafile, trainPerc):
        self.datafile = datafile
        self.trainPerc = trainPerc
        self.validPerc = (1.0 - trainPerc) / 2
        self.rows = []
        self.header = []
        self.instances = []
        self.labels = []
        self.isContinuous = {}
        self.discreteValues = {}


    def readData(self):
        # open the file
        with open(self.datafile, "r") as file:
            reader = csv.reader(file)

            # read in the contents to a list
            self.rows = list(reader)

        # save the header
        self.header = self.rows[DataReader.LABEL_COLUMN]

        # check which columns are continuous
        self.findContinuous()

        # find the values of discrete columns
        self.findDiscreteValues()

        # process the data
        data = []
        for i in range(1, len(self.rows)):
            instance, label = self.process(self.rows[i])

            self.instances.append(instance)
            self.labels.append(label)

        # count the number of attributes and labels
        numAttributes = len(self.instances[0])
        numLabels = len(self.labels[0])

        return numAttributes, numLabels


    def findContinuous(self):
        for col in range(0, len(self.header)):
            # default to True until we find a non-numeric value
            self.isContinuous[col] = True

            for row in self.rows[1:]:
                try:
                    val = float(row[col])
                except ValueError:
                    self.isContinuous[col] = False
                    break


    def findDiscreteValues(self):
        for col in range(len(self.header)):
            if self.isContinuous[col] and col != DataReader.LABEL_COLUMN:
                continue

            # find all possible values of this attribute
            vals = []
            for row in self.rows[1:]:
                val = row[col]
                if val not in vals:
                    vals.append(val)

            # save the possible values
            vals.sort()
            self.discreteValues[col] = vals


    def process(self, row):
        # grab the label
        labelVal = row[DataReader.LABEL_COLUMN]
        if self.isContinuous[DataReader.LABEL_COLUMN]:
            label = [float(labelVal)]
        else:
            label = self.convertLabel(labelVal)

        # grab the instance
        instance = []
        for col in range(len(row)):
            if col == DataReader.LABEL_COLUMN:
                continue

            val = row[col]
            if self.isContinuous[col]:
                # keep the value as a float
                val = float(val)
                instance.append(val)
            else:
                # convert to one hot coding
                vals = self.onehot(col, val)
                instance.extend(vals)

        return instance, label


    def onehot(self, col, val):
        # grab the possible values of this attribute
        possibleVals = self.discreteValues[col]

        # build the one-hot encoding
        vals = [0.0] * (len(possibleVals) - 1)
        if val != possibleVals[-1]:
            vals[possibleVals.index(val)] = 1.0
        return vals


    def convertLabel(self, val):
        # grab the possible labels
        possibleVals = self.discreteValues[DataReader.LABEL_COLUMN]

        # are we binary
        if len(possibleVals) == 2:
            return [1] if val == possibleVals[1] else [0]

        # we are multinomial
        vals = [0] * len(possibleVals)
        vals[possibleVals.index(val)] = 1
        return vals


    def splitData(self):
        # randomize the instances
        num = len(self.instances)
        indices = list(range(num))
        random.shuffle(indices)

        # create the training and test sets
        trainX = []
        trainY = []
        validX = []
        validY = []
        testX = []
        testY = []
        numTrain = (num * self.trainPerc) // 1
        numValid = (num * self.validPerc) // 1

        for i in range(num):
            index = indices[i]

            if i < numTrain:
                trainX.append(self.instances[index])
                trainY.append(self.labels[index])
            elif i < numTrain + numValid:
                validX.append(self.instances[index])
                validY.append(self.labels[index])
            else:
                testX.append(self.instances[index])
                testY.append(self.labels[index])

        # return the train, valid, and test sets as tuples
        return (trainX, trainY), (validX, validY), (testX, testY)