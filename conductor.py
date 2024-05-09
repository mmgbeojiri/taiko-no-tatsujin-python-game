from time import time
from notes_n_classes import *

startTime = time()
songPosition = 0

frame = 0
holdNote = False
def getHoldStatus():
    return holdNote
renders = []
textRenders = []

def getRenders():
    return renders

def getTextRenders():
    return textRenders

def createObject(string, big = 0, doDon = None):
    global renders, holdNote
    if string == "katsu":
        if big == 0:
            renders.append(Blue())
            textRenders.append(Text("ka"))
        else:
            renders.append(Blue(1))
            textRenders.append(Text("bigka"))
    if string == "don":
        if big == 0:
            renders.append(Red())
            if doDon == "Do":
                textRenders.append(Text("do"))
            elif doDon == "Don":
                textRenders.append(Text("don"))
        else:
            renders.append(Red(1))
            textRenders.append(Text("bigdon"))

    if string == "holdstart":
        if big == 0:
            renders.append(HoldStart())
            textRenders.append(Text("drumroll"))
            holdNote = True
        else:
            renders.append(HoldStart(1))
            textRenders.append(Text("bigdrumroll"))

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

def renderNote(noteType, doDon):
    if noteType == "0":
        pass
    elif noteType == "1":
        createObject("don", 0, doDon)
    elif noteType == "2":
        createObject("katsu")
    elif noteType == "3":
        createObject("don", 1)
    elif noteType == "4":
        createObject("katsu", 1)
    elif noteType == "5":
        createObject("holdstart")
    elif noteType == "6":
        createObject("holdstart", 1)
    elif noteType == "8":
        createObject("holdend")
    elif noteType == "7" or noteType == "9":
        print("yea thats never coming here")
    elif noteType == "bar":
        createObject("bar")
    else:
        print(f"cant wtf {noteType}, the type is {type(noteType)}")

