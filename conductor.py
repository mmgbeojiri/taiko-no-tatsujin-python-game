from time import time
from notes_n_classes import *

combo = 0
songStartDebounce = True
startTime = time()
songPosition = 0

frame = 0
holdNote = False
renders = []

def createObject(string, big = 0):
    global renders, holdNote
    if string == "blue":
        if big == 0:
            renders.append(Blue())
        else:
            renders.append(Blue(1))
    if string == "red":
        if big == 0:
            renders.append(Red())
        else:
            renders.append(Red(1))

    if string == "holdstart":
        if big == 0:
            renders.append(HoldStart())
            holdNote = True
        else:
            renders.append(HoldStart(1))
            holdNote = True
    
    if string == "holdmiddle":
        if big == 0:
            renders.append(HoldMiddle())
        else:
            renders.append(HoldMiddle(1))
    
    if string == "holdend":
        if big == 0:
            renders.append(HoldEnd())
            holdNote = False
        else:
            renders.append(HoldEnd(1))
            holdNote = False


    if string == "bar":
        renders.append(Bar())

