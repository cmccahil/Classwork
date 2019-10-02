#concordance.py
#Asks the user for the name of one file. Program opens file and reads it one
#line at a time, counting the line numbers. Each word in the line should be
#stripped of punctuation, in lower-case, and added to concordance w/ line number
#All words that are keys of concordance will be printed in alphabetical order
#along with list of line numbers for each word. At the end the number of unique
#words and the number of lines in the file will be printed
#
#Colin McCahill
#10/15/15
          
def RemovePunctuation(s):
    s=s.strip("`~!@$%^&*()-_=+[{]}\|;:,<.>/?#'"+'"')
    s=s.lower()
    return s

def AddWord(word,L,Concordance):
    #Handling the dictionary
    if word in Concordance.keys():
        Concordance[word].append(L)
    elif word not in Concordance.keys():
        Concordance[word]=[L]
        
def PrintEntry(word,Concordance):
    print(word,end=' ')
    for lineNumber in Concordance[word]:
        print(lineNumber,end=' ')
    print()

def main():
    name=input("What file would you like the concordance for?")
    Concordance={} 
    #reading the file
    F=open(name)
    lineNumber=0
    TotalLines=0
    uniquewords=0
    for line in F:
        strippedLine=line.strip()
        if strippedLine!="":
            TotalLines=TotalLines+1
            lineNumber=lineNumber+1
            wordlist=line.split( )
            for i in wordlist:
                i=RemovePunctuation(i)
                if i!="":
                    AddWord(i,lineNumber,Concordance)
        
        
    words=list(Concordance.keys())
    words.sort()
    for word in words:
        PrintEntry(word,Concordance)
        uniquewords=uniquewords+1
    print("I found",TotalLines,"lines containing",uniquewords,"unique words.")

main()
