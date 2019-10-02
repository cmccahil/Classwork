# middlec.py
# Tom Wexler
# 4/1/13
# Creates and plays a soundwave containing a two-second Middle C note.


import soundwave

def main() :
 
    note = soundwave.Soundwave(0, 2, 1)
    note.play()
    
main()
