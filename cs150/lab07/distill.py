#distill.py
#prompts the user for the name of a text file and a number n, and prints the
#contents of that text file with the n most common words removed.
#
#Colin McCahill
#10/29/2015
def cleanstring(s):
    s=s.strip("`~!@$%^&*()-_=+[{]}\|;:,<.>/?#'"+'"')
    s=s.lower()
    return s

def AddWord(word,Count):
    #Handling the dictionary
    if word in Count.keys():
        Count[word]=Count[word]+1
    elif word not in Count.keys():
        Count[word]=1
def commonlist(Count,n):
    Countlist=[]
    for j in Count.keys():
        Countlist.append((j,Count[j]))
    for k in range(len(Countlist)):
        for m in range(k+1,len(Countlist)): 
            if Countlist[m][1]>Countlist[k][1]: #if the value at index m is bigger than the value at index k
            #switch this with k
                temp=Countlist[k]
                Countlist[k]=Countlist[m]
                Countlist[m]=temp
    commonlistofwords=[]
    for p in range(n):
        commonlistofwords.append((Countlist[p][0]))
    return commonlistofwords
        
def main():
    #interaction with user
    name=input("What text file would you like to open?")
    n=eval(input("How many of the most common words,\"n\", would you like to remove?"))
    Count={} 
    #reading the file
    F=open(name)
    for line in F:
        strippedLine=line.strip()
        if strippedLine!="":
            wordlist=line.split( )
            for i in wordlist:
                i=cleanstring(i)
                if i!="":
                    AddWord(i,Count)
    commonlistofwords=commonlist(Count,n)
    File=open(name)
    for line in File:
        word=line.split( )
        for i in word:
            if i.lower() in commonlistofwords:
                print(" ",end='')
            else:    
                print(i," ",end='')
        print() 
main()
    
    
    
