from gamelib import *
from globalvars import *
from filereader import getSoundFile

songStartDebounce = True
combo = 0
localHealth = 50
drumroll = 0
bulbRenders = []
def getCombo():
    return combo
def getHealth():
    return localHealth
def getBulbRenders():
    return bulbRenders
def getDrumroll():
    return drumroll
def addToBulbRenders(item):
    global bulbRenders, drumroll
    bulbRenders.append(item)
    drumroll += 1




def hitANote(positive = 1):
    global localHealth, combo, game
    if positive > 0:

        combo+=1
    else: 
        combo = 0
    
    localHealth += 5 * positive
    if localHealth > 100:
        localHealth = 100
    if localHealth < 0:
        game.over = False
        # Died
    game.score += 100


# Object Oriented Programming
class Blue: # Katsu
    def __init__(self, big = 0):
        self.object = Image("./images/blue.png", game)
        self.object.resizeTo(960, 540)
        self.big = big
        self.frameCount = 0
        if self.big == 0:
            self.object.resizeBy(drumResize-7)
        else:
            self.object.resizeBy(drumResize+7)
        
        self.object.moveTo(game.width + 100, yPositionLine)
        self.object.setSpeed(scrollSpeed, 90)
    def move(self):
        self.object.move()
        if self.object.x < drumCollide.left - drumHitboxAdd and self.object.visible:
            # Missed
            if self.big == 0:
                hitANote(-1)
            else:
                hitANote(-5)
            self.object.visible = False

    def checkIfHit(self):
        global health
        if self.object.x > drumCollide.left - drumHitboxAdd:
            if self.object.x < drumCollide.right + drumHitboxAdd:
                if self.big == 0:
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            hitANote()
                            bulbRenders.append(self)
                            #self.object.visible = False
                    for i in range(len(outerRightKeys)): # Katsu
                        if keys.Pressed[outerRightKeys[i]]:
                            #self.object.visible = False
                            hitANote()
                            bulbRenders.append(self)
                else:
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            for i in range(len(outerRightKeys)): # Katsu
                                if keys.Pressed[outerRightKeys[i]]:
                                    hitANote(5)
                                    bulbRenders.append(self)
                                    #self.object.visible = False

class Red: # Don
    def __init__(self, big = 0):
        self.object = Image("./images/red.png", game)
        self.object.resizeTo(960, 540)
        self.big = big
        self.frameCount = 0
        if self.big == 0:
            self.object.resizeBy(drumResize-7)
        else:
            self.object.resizeBy(drumResize+7)
        self.object.moveTo(game.width + 100, yPositionLine)
        self.object.setSpeed(scrollSpeed, 90)
    def move(self):
        self.object.move()
        if self.object.x < drumCollide.left - drumHitboxAdd and self.object.visible:
            # Missed
            if self.big == 0:
                hitANote(-1)
            else:
                hitANote(-5)
            self.object.visible = False

    def checkIfHit(self):
        global health
        if self.object.x > drumCollide.left - drumHitboxAdd:
            if self.object.x < drumCollide.right + drumHitboxAdd:
                if self.big == 0:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            hitANote()
                            bulbRenders.append(self)
                            #self.object.visible = False
                    for i in range(len(innerRightKeys)): # Katsu
                        if keys.Pressed[innerRightKeys[i]]:
                            #self.object.visible = False
                            bulbRenders.append(self)
                            hitANote()
                else:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            for i in range(len(innerRightKeys)): # Katsu
                                if keys.Pressed[innerRightKeys[i]]:
                                    hitANote(5)
                                    bulbRenders.append(self)
                                    #self.object.visible = False

class HoldStart:
    def __init__(self, big = 0):
        self.object = Image("./images/holdStart.png", game)
        self.object.resizeTo(960, 540)
        self.big = big
        if self.big == 0:
            self.object.resizeBy(drumResize-7)
        else:
            self.object.resizeBy(drumResize+7)
        self.object.moveTo(game.width + 100, yPositionLine)
        self.object.setSpeed(scrollSpeed, 90)
    def move(self):
        self.object.move()
        if self.object.x < drumCollide.left - drumHitboxAdd and self.object.visible:
            self.object.visible = False

    def checkIfHit(self):
        global health
        if self.object.visible == False:
            return
        redNote = Red()
        redNote.object.x = self.object.x
        blueNote = Blue()
        blueNote.object.x = self.object.x
        if self.object.x > drumCollide.left:
            if self.object.x < drumCollide.right:
                if self.big == 0:
                    for i in range(len(innerLeftKeys)): # Don
                        if keys.Pressed[innerLeftKeys[i]]:
                            hitANote()
                            addToBulbRenders(redNote)
                    for i in range(len(innerRightKeys)): # Don
                        if keys.Pressed[innerRightKeys[i]]:
                            hitANote()
                            addToBulbRenders(redNote)
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            hitANote()
                            addToBulbRenders(blueNote)
                    for i in range(len(outerRightKeys)): # Katsu
                        if keys.Pressed[outerRightKeys[i]]:
                            hitANote()
                            addToBulbRenders(blueNote)

                else:
                    redNote = Red(1)
                    redNote.object.x = self.object.x
                    blueNote = Blue(1)
                    blueNote.object.x = self.object.x
                    for i in range(len(innerLeftKeys)): # Don
                        if keys.Pressed[innerLeftKeys[i]]:
                            for i in range(len(innerRightKeys)):
                                if keys.Pressed[innerRightKeys[i]]:
                                    addToBulbRenders(redNote)
                                    hitANote(5)
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            for i in range(len(outerRightKeys)):
                                if keys.Pressed[outerRightKeys[i]]:
                                    hitANote(5)
                                    addToBulbRenders(blueNote)
class HoldMiddle:
    def __init__(self, big = 0):
        self.object = Image("./images/holdMiddle.png", game)
        self.object.resizeTo(960*1.75, 540)
        self.big = big
        if self.big == 0:
            self.object.resizeBy(drumResize-7)
        else:
            self.object.resizeBy(drumResize+7)
        self.object.moveTo(game.width + 100, yPositionLine)
        self.object.setSpeed(scrollSpeed, 90)
    def move(self):
        self.object.move()
        if self.object.x < drumCollide.left - drumHitboxAdd and self.object.visible:
            self.object.visible = False

    def checkIfHit(self):
        global health
        if self.object.visible == False:
            return
        redNote = Red()
        blueNote = Blue()
        redNote.object.x = self.object.x
        blueNote.object.x = self.object.x
        if self.object.x > drumCollide.left:
            if self.object.x < drumCollide.right:
                if self.big == 0:
                    for i in range(len(innerLeftKeys)): # Don
                        if keys.Pressed[innerLeftKeys[i]]:
                            hitANote()
                            addToBulbRenders(redNote)
                    for i in range(len(innerRightKeys)): # Don
                        if keys.Pressed[innerRightKeys[i]]:
                            hitANote()
                            addToBulbRenders(redNote)
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            hitANote()
                            addToBulbRenders(blueNote)
                    for i in range(len(outerRightKeys)): # Katsu
                        if keys.Pressed[outerRightKeys[i]]:
                            hitANote()
                            addToBulbRenders(blueNote)
                else:
                    redNote = Red(1)
                    redNote.object.x = self.object.x
                    blueNote = Blue(1)
                    blueNote.object.x = self.object.x
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            for i in range(len(innerRightKeys)): 
                                if keys.Pressed[innerRightKeys[i]]:
                                    hitANote(5)
                                    addToBulbRenders(blueNote)
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            for i in range(len(outerRightKeys)):
                                if keys.Pressed[outerRightKeys[i]]:
                                    hitANote(5)
                                    addToBulbRenders(blueNote)
class HoldEnd:
    def __init__(self, big = 0):
        self.object = Image("./images/holdEnd.png", game)
        self.object.resizeTo(960, 540)
        self.big = big
        if self.big == 0:
            self.object.resizeBy(drumResize-7)
        else:
            self.object.resizeBy(drumResize+7)
        self.object.moveTo(game.width + 100, yPositionLine)
        self.object.setSpeed(scrollSpeed, 90)
    def move(self):
        self.object.move()
        if self.object.x < drumCollide.left - drumHitboxAdd and self.object.visible:
            self.object.visible = False

    def checkIfHit(self):
        global health
        if self.object.visible == False:
            return
        redNote = Red()
        blueNote = Blue()
        redNote.object.x = self.object.x
        blueNote.object.x = self.object.x
        if self.object.x > drumCollide.left:
            if self.object.x < drumCollide.right:
                if self.big == 0:
                    for i in range(len(innerLeftKeys)): # Don
                        if keys.Pressed[innerLeftKeys[i]]:
                            hitANote()
                            addToBulbRenders(redNote)
                    for i in range(len(innerRightKeys)): # Don
                        if keys.Pressed[innerRightKeys[i]]:
                            hitANote()
                            addToBulbRenders(redNote)
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            hitANote()
                            addToBulbRenders(blueNote)
                    for i in range(len(outerRightKeys)): # Katsu
                        if keys.Pressed[outerRightKeys[i]]:
                            hitANote()
                            addToBulbRenders(blueNote)
                else:
                    redNote = Red(1)
                    blueNote = Blue(1)
                    redNote.object.x = self.object.x
                    blueNote.object.x = self.object.x
                    for i in range(len(innerLeftKeys)): # Don
                        if keys.Pressed[innerLeftKeys[i]]:
                            for i in range(len(innerRightKeys)):
                                if keys.Pressed[innerRightKeys[i]]:
                                    hitANote(5)
                                    addToBulbRenders(redNote)
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            for i in range(len(outerRightKeys)):
                                if keys.Pressed[outerRightKeys[i]]:
                                    hitANote(5)
                                    addToBulbRenders(blueNote)
music = Sound(getSoundFile(), 6)


class Bar:
    def __init__(self):
        self.object = Image("./images/bar.png", game)
        self.object.resizeBy(-73)
        self.object.moveTo(game.width + 100, yPositionLine)
        self.object.setSpeed(scrollSpeed, 90)

    def move(self):
        global songStartDebounce
        self.object.move()
        if self.object.x < drumCollide.x:
            if songStartDebounce:
                print("play the Music")
                music.play()
                songStartDebounce = False
    def checkIfHit(self):
        pass
        # We do a pass to not cause an error since this is in the render
    
class Text:
    def __init__(self, text = "Don"):
        self.string = text
        self.x = game.width + 100 
        self.y = yPositionLine + 50
    def move(self):
        self.x -= scrollSpeed
        
    
