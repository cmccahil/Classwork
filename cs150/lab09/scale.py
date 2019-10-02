#scale.py
#play a scale speciefied by two input from the user: the tonic note as a
#semitone offset from middle C, and a choice of scale
#
#Colin McCahill
#11/16/15

import soundwave

def main():
    done=False
    while not done:
        scale=input("Give a mode of a scale (major, minor, blues, or quit): ")
        if scale=="quit":
            done=True
        elif scale=="major":
            t=input("Give an offset number from middle C: ")
            try:
                t=eval(t)
                intervals=[t,t+2,t+4,t+5,t+7,t+9,t+11,t+12]
                dur=.3
                music=soundwave.Soundwave()
                notes=[]
                for i in intervals:
                    notes.append(soundwave.Soundwave(i,dur))
                for j in notes:
                    music.concat(j)
                music.play()
            except:
                print("That is not a number")
        elif scale=="minor":
            t=input("Give an offset number from middle C: ")
            try:
                t=eval(t)
                intervals=[t,t+2,t+3,t+5,t+7,t+8,t+10,t+12]
                dur=.3
                music=soundwave.Soundwave()
                notes=[]
                for i in intervals:
                    notes.append(soundwave.Soundwave(i,dur))
                for j in notes:
                    music.concat(j)
                music.play()
            except:
                print("That is not a number")
        elif scale=="blues":
            t=input("Give an offset number from middle C: ")
            try:
                t=eval(t)
                intervals=[t,t+3,t+5,t+6,t+7,t+10,t+12]
                dur=.3
                music=soundwave.Soundwave()
                notes=[]
                for i in intervals:
                    notes.append(soundwave.Soundwave(i,dur))
                for j in notes:
                    music.concat(j)
                music.play()
            except:
                print("That is not a number")
        else:
            print("Not a valid input")
main()
    
