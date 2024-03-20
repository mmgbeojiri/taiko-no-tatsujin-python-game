from time import time
from notes_n_classes import *

startTime = time()
songPosition = 0

frame = 0
holdNote = False
def getHoldStatus():
    return holdNote
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

def renderNote(noteType):
    if noteType == 0:
        pass
    if noteType == 1:
        createObject("don")
    if noteType == 2:
        createObject("katsu")
    if noteType == 3:
        createObject("don", 1)
    if noteType == 4:
        createObject("katsu", 1)
    if noteType == 5:
        createObject("holdstart")
    if noteType == 6:
        createObject("holdstart", 1)
    if noteType == 8:
        createObject("holdend")
    if noteType == 7 or noteType == 9:
        print("yea thats never coming here")

