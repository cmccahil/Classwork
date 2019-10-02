#soundwave.py
#a Soundwave class that lets Soundfiles and sound programs play 
#
#Colin McCahill
#11/12/2015

import audio
import math

class Soundwave:
    
    def __init__(self,halftones=0,duration=0,amp=1,samplerate=44100):
        if isinstance(halftones,str):
            self.samples=audio.read_file(halftones)
        else:
            self.samples=[]
            freq=440*(2**((halftones+3)/12))
            for t in range(int(duration*samplerate//1)):
                self.samples.append(amp*math.sin(2*math.pi*freq*t/samplerate))
    
    def play(self):
        audio.play(self.samples)
        
    def concat(self,s2):
        self.samples.extend(s2.samples)

    def plus(self,s2):
        new=Soundwave(0,0,1,44100)
        if len(self.samples)>=len(s2.samples):
            for i in range(len(s2.samples)):
                new.samples.append(self.samples[i]+s2.samples[i])
            new.samples.extend(self.samples[len(s2.samples):len(self.samples)])
        else:
            for i in range(len(self.samples)):
                new.samples.append(self.samples[i]+s2.samples[i])
            new.samples.extend(s2.samples[len(self.samples):len(s2.samples)])
        return new
    
        

        
