#morseDecoder.py
#translates Morse Code into Standard letters
#
#Colin McCahill
#11/4/15

def decode(code,Table):
    for pair in Table:
        if code==pair[1]:
            print(pair[0],end='')
        
def main():
    F=open("MorseTable.txt")
    Table=[]
    for line in F:
        line=line.split()
        Table.append(line)
    G=open("MorseMessage.txt")
    for line in G:
        if len(line)==0:
            del(line)
        else:
            l=line.split("  ")
        for word in l:
            w=word.split(" ")
            for letter in w:
                decode(letter,Table)
            print(" ",end='')
        print()
            
main()
