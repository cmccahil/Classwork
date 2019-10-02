#anagrams.py
#reads in a file so it knows what strings are words in English, and then reads
#phrases from the user and prints anagrams for them
#
#Colin McCahill
#11/1/15

def contains(s,word):
    for letter in word:
        if letter not in s:
            return False, ""
        else:
            s=s.replace(letter, "", 1)
    return (True, s)

def grams(s,words,sofar):
    if s=="":
        for i in sofar:
            print(i,"",end='')
        print()
    else:
        for word in words:
            #3. contains function
            containsfunction=contains(s,word)
            if containsfunction[0]==True:
                far = []
                for x in sofar:
                    far.append(x)
                far.append(word)
                grams(containsfunction[1],words,far)
        
    
def main():
    File=input("What dictionary file would you like to use? ")
    done=False
    while not done:
        string=input("Give a string or type enter to quit program:")
        if string=="":
            done=True
        else:
            #1.creating the new string
            splitwords=string.split()
            newstring=""
            for i in splitwords:
                newstring=newstring+i
            #2.building the set
            F=open(File)
            wordlist=set()
            for line in F:
                line=line.strip()
                wordlist.add(line)
            #4.grams function
            sofar=[]
            grams(newstring,wordlist,sofar)
main() 
                
