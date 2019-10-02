#Decrypt.py
#decode a file that has been encoded with a Caesar cypher
#
#Colin McCahill
#11/05/15

def ord(c):
    letters=[]
    for x in "abcdefghijklmnopqrstuvwxyz":
        letters.append(x)
    for i in range(26):
        if c==letters[i]:
            return(i)
        
def chr(n,oppositedifference):
    n=n+oppositedifference
    if n>25:
        n=n%26
    return n

def shiftletter(c):
    letters=[]
    for x in "abcdefghijklmnopqrstuvwxyz":
        letters.append(x)
    return letters[c]

def occurences(F):
    Counts=[]
    for k in range(26):
        Counts.append(0)
    for line in F:
        l=line.split()
        for word in line:
            w=word.split(" ")
            indexnumber=ord(w[0])
            if indexnumber!=None:
                Counts[indexnumber]=Counts[indexnumber]+1
    return Counts

def main():
    File=input("Name of encoded File: ")
    F=open(File)
    Counts=occurences(F)
    #this finds the difference between the index of the biggest number and the index of e
    prev=0 #a placeholder
    for i in range(len(Counts)):
        if Counts[i]>Counts[prev]:
            prev=i #prev now=largest index value in the list
    difference=prev-4
    oppositedifference=26-difference
    F=open(File)
    for line in F:
        l=line.split()
        for word in line:
            w=word.split()
            if w==[]:
                print(" ",end='')
            else:
                indexnumber=ord(w[0])
                if indexnumber!=None:
                    #This is where it shifts the letter
                    newindex=chr(indexnumber,oppositedifference)
                    newletter=shiftletter(newindex)
                    w[0]=newletter
                print(w[0],end='')
        print()
main()
