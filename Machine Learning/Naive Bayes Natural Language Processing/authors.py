from nltk.corpus import stopwords
import StemmingUtil
import sys
import numpy as np

books = ["AliceInWonderland.txt", "AnnaKarenina.txt", "GreatExpectations.txt",
         "PrideAndPrejudice.txt", "RomeoAndJuliet.txt", "TheAdventuresOfSherlockHolmes.txt",
         "TheOdyssey.txt", "TheRepublic.txt", "TheTrial.txt", "TheWarOfTheWorlds.txt"]


def count_in_book(word, book, texts):
    i = books.index(book)
    text = texts[i]
    stems = StemmingUtil.createStems(word)
    return text.count("".join(stems))

def remove_punctuation(word):
    punctuation = ',:.?!-&%/()\"\'@<>'
    result = word.lower()
    for x in result:
        if x in punctuation:
            result = result.replace(x, "")
    return result

def findOriginalWords(books):
    print("Finding unique words")
    booksCombined = []
    for book in books:
        booksCombined = booksCombined + book
    return len(set(booksCombined))

def NaiveBayes(test,training,authors,uniqueWords):
    predictedLabels = []
    for i in range(0,len(test)):
        labelProb = [0,0,0,0,0,0,0,0,0,0]
        for j in range(0,len(test[i])):
            
            for k in range(0,len(books)):
                countInBook = count_in_book(test[i][j],books[k],training)
                totalWordsInBook = len(training[k])
                if(countInBook == 0): #here we must implement pseudocounts 
                    labelProb[k] += np.log(1/(totalWordsInBook + uniqueWords)) #is 10 the right number?
                #print(test[i][j])
                #print(countInBook)
                #print(len(training[k]))
                
                #print(np.log(countInBook/totalWordsInBook))
                labelProb[k] += np.log((countInBook+1)/(totalWordsInBook + uniqueWords))
        for j in range(0,len(labelProb)):
            labelProb[j] += np.log(1/10)
        #print(labelProb)
        maxIndex = labelProb.index(max(labelProb))
        predictedLabels.append(authors[maxIndex])
    print("Predicted Labels",predictedLabels)
    return predictedLabels
            

def preprocessing(book):
    stop_words = set(stopwords.words('english'))
    print("Parsing:", book)
    file = open(book, errors='ignore')
    allWords = []
    for line in file:
        for word in line.split():
            lowercase = remove_punctuation(word)
            if lowercase not in stop_words:
                allWords.append(lowercase)
    stems = StemmingUtil.createStems(allWords)
    return stems

def testSetPreprocessing(file):
    stop_words = set(stopwords.words('english'))
    labels = []
    passages = []
    with open(file,errors='ignore') as f: #parsing test file passages
        for line in f:
            if(line[0] == '#'):
                continue
            else:
                words = line.split()
                if(len(words) == 1):
                    labels.append(words[0])
                else:
                    passage = []
                    for word in words:
                        lowercase = remove_punctuation(word)
                        if lowercase not in stop_words:
                            passage.append(lowercase)
                    passages.append(passage)
    with open("HamletPassages.txt",errors='ignore') as f: #this will be our book
        for line in f:
            labels.append("Shakespeare")
            words= line.split()
            passage = []
            for word in words:
                lowercase = remove_punctuation(word)
                if lowercase not in stop_words:
                    passage.append(lowercase)
            passages.append(passage)
            
    print(labels)
    print(passages)
    return labels,passages
        

def main():
    books = ["AliceInWonderland.txt", "AnnaKarenina.txt", "GreatExpectations.txt",
             "PrideAndPrejudice.txt", "RomeoAndJuliet.txt", "TheAdventuresOfSherlockHolmes.txt",
             "TheOdyssey.txt", "TheRepublic.txt", "TheTrial.txt", "TheWarOfTheWorlds.txt"]
    authors = ["Caroll","Tolstoy","Dickens","Austen","Shakespeare",
               "Doyle","Homer","Plato","Kafka","Wells"]
    actualLabels,testPassages = testSetPreprocessing(sys.argv[1])
    texts = []
    for book in books:
        texts.append(preprocessing(book))
    uniqueWords = findOriginalWords(texts)
    print(uniqueWords)
    print(actualLabels)
    predictedLabels = NaiveBayes(testPassages,texts,authors,uniqueWords)

    numberOfPredictionsRight = 0
    for i in range(len(predictedLabels)):
        if(predictedLabels[i] == actualLabels[i]):
            numberOfPredictionsRight += 1
    print("Accuracy: ",numberOfPredictionsRight/len(predictedLabels))


if __name__ == '__main__':
    main()
