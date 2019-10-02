#mastermind.py
#Allows user to play a text based version of the fantastic game Mastermind
#
#Colin McCahill
#09/26/15

import random

def generateCode():
    #this generates a random code
    color="RGBYPO"
    #use this for an index
    code=""
    for i in range(4):
        n=random.randint(0,5)
        code=code+color[n]
    return code


def evaluateGuess(code,guess):
    #this takes the guess given by the user and evaluates it against the actual
    #guess
    #blackpegs
    blackpegs=0
    for i in range(4):
        if (code[i]==guess[i]):
            code=code[0:i]+"w"+code[i+1:]
            guess=guess[0:i]+"x"+guess[i+1:]
            blackpegs=blackpegs+1

    #whitepegs
    whitepegs=0
    for i in range(4):
        for j in range(4):
            if guess[i]==code[j]:
                code=code[0:j]+"u"+code[j+1:]
                guess=guess[0:i]+"z"+guess[i+1:]
                whitepegs=whitepegs+1
    return blackpegs,whitepegs            

def main():
    NUM_TURNS=10
    code=generateCode()
    print("I have a 4 letter code, made from 6 colors.")
    print("The colors are R, G, B, Y, P, or O.")
    print()
    done=False
    while NUM_TURNS>0 and not done:
        guess=input("   Your guess:")
        black,white=evaluateGuess(code,guess)
        print("Not quite. You get",black,"black pegs,",white,"white pegs.")
        print()
        NUM_TURNS=NUM_TURNS-1
        if code==guess:
            print("You win! Aren't you smart.")
            done=True
        if NUM_TURNS==0:
            print("Sorry, you lose! The correct code was",code)

main()
        
    



