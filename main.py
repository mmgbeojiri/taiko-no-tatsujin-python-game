from gamelib import *
import time
from random import randint

'''
# Initialize debounce flags for each key
debounce_flags = {
    key: False for key in outerLeftKeys + outerRightKeys + innerLeftKeys + innerRightKeys
}

# Inside the game loop, handle key press events
for key in debounce_flags:
    if keys.Pressed[key] and not debounce_flags[key]:  # Check if key is pressed and debounce flag is False
        debounce_flags[key] = True  # Set debounce flag to True to prevent multiple plays
        # Play corresponding sound based on key
        if key in innerLeftKeys or key in innerRightKeys:  # Don sound
            don_sound.play()
        else:  # Katsu sound
            katsu_sound.play()
    elif not keys.Pressed[key] and debounce_flags[key]:  # Check if key is released and debounce flag is True
        debounce_flags[key] = False  # Reset debounce flag
'''

game = Game(1920, 1080, "Taiko no Tatsujin - Python")

outerBar = Image("./images/outerbar.png", game)
innerBar = Image("./images/innerbar.png", game)

outerBar.resizeBy(100)
innerBar.resizeBy(100)

yPositionLine = 153
drumResize = -78

scoreContain = Image("./images/scorecontainer.png", game)

scoreContain.resizeBy(-57)
scoreContain.moveTo(scoreContain.width/2, yPositionLine)


drum = Image("./images/taikodrum.png", game)
drumCollide = Image("./images/drumhit.png", game)

drum.resizeBy(drumResize)
drumCollide.resizeBy(drumResize)


drum.moveTo(scoreContain.width - 100, yPositionLine)
drumCollide.moveTo(drum.x + 200, yPositionLine)
beatLine = drumCollide.x

drumInnerRight = Image("./images/drum/innerright.png", game)
drumInnerLeft = Image("./images/drum/innerleft.png", game)
drumOuterRight = Image("./images/drum/outerright.png", game)
drumOuterLeft = Image("./images/drum/outerleft.png", game)



drumInnerRight.moveTo(drum.x, drum.y)
drumInnerLeft.moveTo(drum.x, drum.y)
drumOuterRight.moveTo(drum.x, drum.y)
drumOuterLeft.moveTo(drum.x, drum.y)

blue = Image("./images/blue.png", game)
red = Image("./images/red.png", game)
effect = Image("./images/effect.png", game)
effect.resizeTo(5, 5)

drumInnerRight.resizeBy(drumResize)
drumInnerLeft.resizeBy(drumResize)
drumOuterRight.resizeBy(drumResize)
drumOuterLeft.resizeBy(drumResize)

don = Sound("./sounds/Don.wav", 1)
katsu = Sound("./sounds/Katsu.wav", 2)

health = 50
barMultipler = 9
yellowHealth = Shape("bar", game, health * barMultipler, 20, yellow)
greenHealth = Shape("bar", game, health * barMultipler, 20, green)

scrollSpeed = 10
drumHitboxAdd = 5
def hitEffect():
    global drumCollide, effect
    effect.resizeTo(78, 78)
    effect.resizeBy(130)


outerLeftKeys = [
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_q,
    K_w,
    K_e, 
    K_r,
    K_t
]

outerRightKeys = [
    K_6,
    K_7,
    K_8,
    K_9,
    K_0,
    K_y,
    K_u,
    K_i,
    K_o,
    K_p
]

innerLeftKeys = [
    K_a,
    K_s,
    K_d,
    K_f,
    K_g,
    K_z,
    K_x,
    K_c,
    K_v,
    K_b,
]

innerRightKeys = [
    K_h,
    K_j,
    K_k,
    K_l,
    K_SEMICOLON,
    K_n,
    K_m,
    K_COMMA,
    K_PERIOD
]

# Initialize debounce flags for each key
debounce_flags = {
    key: False for key in outerLeftKeys + outerRightKeys + innerLeftKeys + innerRightKeys
}

combo = 0

def hitANote(positive = 1):
    global health, combo, game
    if positive > 0:

        combo+=1
    else: 
        combo = 0
    
    health+= 5 * positive
    if health > 100:
        health = 100
    if health < 0:
        game.over = False
        # Died
    game.score += 100

# Object Oriented Programming
class Blue: # Katsu
    def __init__(self, big = 0):
        self.object = Image("./images/blue.png", game)
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
            # Missed
            hitANote(-1)
            self.object.visible = False
    def checkIfHit(self):
        global health
        if self.object.x > drumCollide.left - drumHitboxAdd:
            if self.object.x < drumCollide.right + drumHitboxAdd:
                if self.big == 0:
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            hitANote()
                            self.object.visible = False
                    for i in range(len(outerRightKeys)): # Katsu
                        if keys.Pressed[outerRightKeys[i]]:
                            self.object.visible = False
                            hitANote()
                else:
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            for i in range(len(outerRightKeys)): # Katsu
                                if keys.Pressed[outerRightKeys[i]]:
                                    hitANote(5)
                                    self.object.visible = False




class Red: # Don
    def __init__(self, big = 0):
        self.object = Image("./images/red.png", game)
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
            # Missed
            hitANote(-1)
            self.object.visible = False

    def checkIfHit(self):
        global health
        if self.object.x > drumCollide.left - drumHitboxAdd:
            if self.object.x < drumCollide.right + drumHitboxAdd:
                if self.big == 0:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            hitANote()
                            self.object.visible = False
                    for i in range(len(innerRightKeys)): # Katsu
                        if keys.Pressed[innerRightKeys[i]]:
                            self.object.visible = False
                            hitANote()
                else:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            for i in range(len(innerRightKeys)): # Katsu
                                if keys.Pressed[innerRightKeys[i]]:
                                    hitANote(5)
                                    self.object.visible = False

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
            # Missed
            hitANote(-1)
            self.object.visible = False

    def checkIfHit(self):
        global health
        if self.object.x > drumCollide.left - drumHitboxAdd:
            if self.object.x < drumCollide.right + drumHitboxAdd:
                if self.big == 0:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            hitANote()
                            self.object.visible = False
                    for i in range(len(innerRightKeys)): # Katsu
                        if keys.Pressed[innerRightKeys[i]]:
                            self.object.visible = False
                            hitANote()
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            hitANote()
                            self.object.visible = False
                    for i in range(len(outerRightKeys)): # Katsu
                        if keys.Pressed[outerRightKeys[i]]:
                            self.object.visible = False
                            hitANote()
                else:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            for i in range(len(innerRightKeys)): # Katsu
                                if keys.Pressed[innerRightKeys[i]]:
                                    hitANote(5)
                                    self.object.visible = False
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            for i in range(len(outerRightKeys)): # Katsu
                                if keys.Pressed[outerRightKeys[i]]:
                                    hitANote(5)
                                    self.object.visible = False                                    
class HoldMiddle:
    def __init__(self, big = 0):
        self.object = Image("./images/holdMiddle.png", game)
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
            # Missed
            hitANote(-1)
            self.object.visible = False

    def checkIfHit(self):
        global health
        if self.object.x > drumCollide.left - drumHitboxAdd:
            if self.object.x < drumCollide.right + drumHitboxAdd:
                if self.big == 0:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            hitANote()
                            self.object.visible = False
                    for i in range(len(innerRightKeys)): # Katsu
                        if keys.Pressed[innerRightKeys[i]]:
                            self.object.visible = False
                            hitANote()
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            hitANote()
                            self.object.visible = False
                    for i in range(len(outerRightKeys)): # Katsu
                        if keys.Pressed[outerRightKeys[i]]:
                            self.object.visible = False
                            hitANote()
                else:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            for i in range(len(innerRightKeys)): # Katsu
                                if keys.Pressed[innerRightKeys[i]]:
                                    hitANote(5)
                                    self.object.visible = False
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            for i in range(len(outerRightKeys)): # Katsu
                                if keys.Pressed[outerRightKeys[i]]:
                                    hitANote(5)
                                    self.object.visible = False   
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
            # Missed
            hitANote(-1)
            self.object.visible = False

    def checkIfHit(self):
        global health
        if self.object.x > drumCollide.left - drumHitboxAdd:
            if self.object.x < drumCollide.right + drumHitboxAdd:
                if self.big == 0:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            hitANote()
                            self.object.visible = False
                    for i in range(len(innerRightKeys)): # Katsu
                        if keys.Pressed[innerRightKeys[i]]:
                            self.object.visible = False
                            hitANote()
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            hitANote()
                            self.object.visible = False
                    for i in range(len(outerRightKeys)): # Katsu
                        if keys.Pressed[outerRightKeys[i]]:
                            self.object.visible = False
                            hitANote()
                else:
                    for i in range(len(innerLeftKeys)): # Katsu
                        if keys.Pressed[innerLeftKeys[i]]:
                            for i in range(len(innerRightKeys)): # Katsu
                                if keys.Pressed[innerRightKeys[i]]:
                                    hitANote(5)
                                    self.object.visible = False
                    for i in range(len(outerLeftKeys)): # Katsu
                        if keys.Pressed[outerLeftKeys[i]]:
                            for i in range(len(outerRightKeys)): # Katsu
                                if keys.Pressed[outerRightKeys[i]]:
                                    hitANote(5)
                                    self.object.visible = False   

songStartDebounce = True
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
                songStartDebounce = False
    def checkIfHit(self):
        pass
        # We do a pass to not cause an error since this is in the render



def createObject(string, big = 0):
    global renders, Blue
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
        else:
            renders.append(HoldStart(1))
    
    if string == "holdmiddle":
        if big == 0:
            renders.append(HoldMiddle())
        else:
            renders.append(HoldMiddle(1))
    
    if string == "holdend":
        if big == 0:
            renders.append(HoldEnd())
        else:
            renders.append(HoldEnd(1))


    if string == "bar":
        renders.append(Bar())


startTime = time.time()
songPosition = 0
frame = 0
renders = []
while not game.over:
    game.processInput()
    game.clearBackground()
    outerBar.draw()

    if health < 50:
        yellowHealth.width = health * barMultipler
    else:
        yellowHealth.width = 50 * barMultipler

    if health > 50:
        greenHealth.width = health/2 * barMultipler
    else:
        greenHealth.width = 0


    yellowHealth.moveTo(0, scoreContain.top)

    greenHealth.moveTo(yellowHealth.x + (50*barMultipler), yellowHealth.y)
    yellowHealth.draw()
    greenHealth.draw()

    innerBar.draw()
    effect.draw()
    effect.resizeBy(-2)
    effect.moveTo(drumCollide.x, drumCollide.y)
    drumCollide.draw()

    # Notes #
    print(round(songPosition, 5) % 1)
    if frame == 0:
        createObject("bar")

    if frame == 0:
        if randint(1, 2) == 1:
            randomNum = randint(1, 5)
            if randomNum == 1:
                createObject("blue")
            if randomNum == 2:
                createObject("red")
            if randomNum == 3:
                createObject("bigblue")
            if randomNum == 4:
                createObject("bigred")
            if randomNum == 5:
                createObject("holdStart")

    if frame == 15:
        if randint(1, 2) == 1:
            randomNum = randint(1, 5)
            if randomNum == 1:
                createObject("blue")
            if randomNum == 2:
                createObject("red")
            if randomNum == 3:
                createObject("bigblue")
            if randomNum == 4:
                createObject("bigred")
            if randomNum == 5:
                createObject("holdStart")

    if frame == 30:
        if randint(1, 2) == 1:
            randomNum = randint(1, 5)
            if randomNum == 1:
                createObject("blue")
            if randomNum == 2:
                createObject("red")
            if randomNum == 3:
                createObject("bigblue")
            if randomNum == 4:
                createObject("bigred")
            if randomNum == 5:
                createObject("holdStart")
                
    if frame == 45:
        if randint(1, 2) == 1:
            randomNum = randint(1, 5)
            if randomNum == 1:
                createObject("blue")
            if randomNum == 2:
                createObject("red")
            if randomNum == 3:
                createObject("bigblue")
            if randomNum == 4:
                createObject("bigred")
            if randomNum == 5:
                createObject("holdStart") 

    for i in range(len(renders)):
        renders[i].move()

    scoreContain.draw()
    game.drawText(f"{game.score}", drum.left - 100, yPositionLine)
    game.drawText(f"combo: {combo}", drum.left - 100, yPositionLine+50)
    drum.draw()


    for i in range(len(outerLeftKeys)): # Katsu
        if keys.Pressed[outerLeftKeys[i]]:
            drumOuterLeft.draw()
    for i in range(len(outerRightKeys)): # Katsu
        if keys.Pressed[outerRightKeys[i]]:
            drumOuterRight.draw()
    for i in range(len(innerLeftKeys)): # Don
        if keys.Pressed[innerLeftKeys[i]]:
            drumInnerLeft.draw()
    for i in range(len(innerRightKeys)): # Don
        if keys.Pressed[innerRightKeys[i]]:
            drumInnerRight.draw()
    
    # for each key, make a sound debounce. when key is pressed, play sound only once. 

    # Inside the game loop, handle key press events
    for key in debounce_flags:
        if keys.Pressed[key] and not debounce_flags[key]:  # Check if key is pressed and debounce flag is False
            hitEffect()
            for i in range(len(renders)):
                renders[i].checkIfHit()
            debounce_flags[key] = True  # Set debounce flag to True to prevent multiple plays
            # Play corresponding sound based on key
            if key in innerLeftKeys or key in innerRightKeys:  # Don sound
                don.play()
            else:  # Katsu sound
                katsu.play()
        elif not keys.Pressed[key] and debounce_flags[key]:  # Check if key is released and debounce flag is True
            debounce_flags[key] = False  # Reset debounce flag



    songPosition = (time.time() - startTime)
    frame += 1
    if frame == 60:
        frame = 0
    game.update(60)
game.quit()