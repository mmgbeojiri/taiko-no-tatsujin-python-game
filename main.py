from random import randint
from gamelib import *
from globalvars import * # All the Global Variables (Defining the inital keys and sprites)
from notes_n_classes import * # All the Note Types and Classes (available for cloning)
from filereader import * # responsible for reading the chart
from conductor import * # responsible for rendering notes from the filereaders
from math import cos
from math import pi

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

donWadaNormal = Animation("./images/donWada/normalBop.png", 4, game, 370, 251, 8)
donWadaGogo = Animation("./images/donWada/gogoBopLongWithCrop.png", 8, game, 370, 251, 4)
donWadaSurvival = Animation("./images/donWada/survivalBop.png", 4, game, 370, 251, 8)
donWadaRotate = Animation("./images/donWada/rotate.png", 5, game, 370, 251, 2)
donWadaSurvivalFall = Animation("./images/donWada/survivalfall.png", 1, game, 370, 251, 8)
donWadaBarJump = Animation("./images/donWada/barJump.png", 1, game, 370, 251, 8)

donState = "Normal"

donX = game.width/2
donY = game.height/2
donYVel = 0
donYGround = donY


blueTransparentImage = pygame.image.load("./images/blue.png").convert()
redTransparentImage = pygame.image.load("./images/red.png").convert()

barDebounce = True

def ChangeDonState(string):
    global donState, donRelativeY
    donState = string

def barJump(type = "Nonset"):
    global donYVel, donState
    if donState == "Normal":
        ChangeDonState("BarJump")
    if donState == "Survival":
        ChangeDonState("Transition")
    if not type == "Nonset":
        ChangeDonState(type) 
    donYVel = -15

def UpdateBulbNotes():
    global blueTransparentImage, redTransparentImage
    bulbRenders = getBulbRenders()
    for i in range(len(bulbRenders)):
        if bulbRenders[i] not in getRenders():
            bulbRenders[i].object.draw()
        if bulbRenders[i].object.visible:
            bulbRenders[i].object.setSpeed(0,0)
            bulbRenders[i].object.x += (bulbx - bulbRenders[i].object.x) / 16
            bulbRenders[i].object.y -= (bulbRenders[i].object.y-bulby) / 16

            if round(bulbRenders[i].object.x) == round(bulbx):
                if round(bulbRenders[i].object.y) == round(bulby):
                    bulbRenders[i].frameCount += 8

                    if str(bulbRenders[i].__class__) == "<class 'notes_n_classes.Blue'>":
                        note = "blue"

                    if str(bulbRenders[i].__class__) == "<class 'notes_n_classes.Red'>":
                        note = "red"
                    
                    if note == "blue":
                        blueTransparentImage = pygame.transform.scale(blueTransparentImage,(int(bulbRenders[i].object.width),int(bulbRenders[i].object.height)))
                        blueTransparentImage.set_alpha(255 - (bulbRenders[i].frameCount*2))
                        bulbRenders[i].object.setImage(blueTransparentImage)
                    if note == "red":
                        redTransparentImage = pygame.transform.scale(redTransparentImage,(int(bulbRenders[i].object.width),int(bulbRenders[i].object.height)))
                        redTransparentImage.set_alpha(255 - (bulbRenders[i].frameCount*2))
                        bulbRenders[i].object.setImage(redTransparentImage)
                    

                    if bulbRenders[i].frameCount >= 128:

                        bulbRenders[i].object.visible = False

    
def CheckIfShouldBeHold():
    global holdNote, frame
    if getHoldStatus() == True and frame % 8 == 0:
        createObject("holdmiddle")

# Title Screen #
while not game.over:
    game.processInput()
    game.clearBackground()

    logo.moveTo(game.width/2, math.sin((0.1/60)*frame)*2 - game.height/4)

    clickAnywhere.draw()
    frame += 1
    if frame >= 60:
        frame = 0 

    game.update(60)
game.over = False

# Game #
while not game.over:
    game.processInput()
    game.clearBackground()
    outerBar.draw()
    health = getHealth()
    combo = getCombo()
    if combo > maxCombo:
        maxCombo = combo
    if health < 50:
        yellowHealth.width = health * barMultipler
    else:
        yellowHealth.width = 50 * barMultipler

    if health > 50:
        greenHealth.width = health/2 * barMultipler
    else:
        greenHealth.width = 0

    donWadaNormal.moveTo(donX, donY)
    donWadaGogo.moveTo(donX, donY)
    donWadaSurvival.moveTo(donX, donY)
    donWadaRotate.moveTo(donX, donY)
    donWadaSurvivalFall.moveTo(donX, donY)
    donWadaBarJump.moveTo(donX, donY)

    donWadaNormal.visible = False
    donWadaGogo.visible = False
    donWadaSurvival.visible = False
    donWadaRotate.visible = False
    donWadaSurvivalFall.visible = False
    donWadaBarJump.visible = False

    if donState == "Normal":
        donWadaNormal.visible = True
    if donState == "Gogo":
        donWadaGogo.visible = True
    if donState == "Survival":
        donWadaSurvival.visible = True
    if donState == "Transition":
        donWadaRotate.visible = True
    if donState == "SurvivalFall":
        donWadaSurvivalFall.visible = True
    if donState == "BarJump":
        donWadaBarJump.visible = True

    if keys.Pressed[K_SPACE]: # Transition to Survival
        barJump()

    # Gravity #
    donYVel += 1

    # Floor Collision #
    if round(donY) > donYGround:
        donY = donYGround
        donYVel = 0
    else:
        donY += donYVel

    if donState == "Transition" or donState == "BarJump" or donState == "SurvivalFall": #if not stateemnent
        pass
    else:
        if getGogoMode():
            ChangeDonState("Gogo")
        elif health > 50:
            ChangeDonState("Survival")
        else:
            ChangeDonState("Normal")
    
    # Falling #
    if donYVel > 0:
        if donState == "Transition":
            ChangeDonState("SurvivalFall")

        
    # Landing #
    if round(donY) == donYGround:
        if donState == "SurvivalFall":
            ChangeDonState("Survival")
        if donState == "BarJump":
            ChangeDonState("Normal")

    #Check every Frame
 

    yellowHealthContainer.moveTo(0, scoreContain.top-(yellowHealthContainer.height/2))
    greenHealthContainer.moveTo(yellowHealth.x + (50*barMultipler), yellowHealthContainer.y - (greenHealthContainer.height - yellowHealthContainer.height))

    yellowHealth.moveTo(yellowHealthContainer.x + 5, yellowHealthContainer.y+5)

    greenHealth.moveTo(greenHealthContainer.x, greenHealthContainer.y+5)
    yellowHealth.draw()
    greenHealth.draw()

    innerBar.draw()
    okEffect.draw()
    okEffect.resizeBy(-2)
    okEffect.moveTo(drumCollide.x, drumCollide.y)
    
    badEffect.draw()
    badEffect.resizeBy(-2)
    badEffect.moveTo(drumCollide.x, drumCollide.y)

    goodEffect.draw()
    goodEffect.resizeBy(-2)
    goodEffect.moveTo(drumCollide.x, drumCollide.y)

    drumCollide.draw()

    for i in range(len(getTextRenders())):
        textObject = getTextRenders()[i]
        textObject.move()
        textObject.object.draw()

    # Inside the game loop, handle key press events
    renders = getRenders()
    for key in debounce_flags:
        if keys.Pressed[key]:
            if not debounce_flags[key]:  # Check if key is pressed and debounce flag is False
                debounce_flags[key] = True  # Set debounce flag to True to prevent multiple plays
                for i in range(len(renders)):
                    if renders[i].checkIfHit():
                        hitEffect(calculatehitDistance(renders[i]))
                # Play corresponding sound based on key
                if key in innerLeftKeys or key in innerRightKeys:  # Don sound
                    don.play()
                else:  # Katsu sound
                    katsu.play()

    

    # Notes #
    '''
    if frame == 0:
        createObject("bar")
    holdNote = getHoldStatus()
    if frame % 15 == 0:
        if randint(1, 2) == 1:
            randomNum = randint(1, 6)
            if holdNote == False:
                if randomNum == 1:
                    createObject("blue")
                if randomNum == 2:
                    createObject("red")
                if randomNum == 3:
                    createObject("blue", 1)
                if randomNum == 4:
                    createObject("red", 1)
                if randomNum == 5:
                    createObject("holdstart")
                    
            if holdNote == True:
                if randomNum == 6 or randomNum == 2 or randomNum == 4:
                    createObject("holdend")
                    holdNote = False
    '''


    for i in range(len(getRenders())):
        getRenders()[i].move()
        if str(getRenders()[i].__class__) == "<class 'notes_n_classes.Bar'>":
            if getRenders()[i].object.collidedWith(drumCollide):
                if donY < donYGround: # if don is already jumping
                    pass
                else:
                    if abs(drumCollide.x - getRenders()[i].object.x) <= 30:
                        if barDebounce == True:
                            if not donState == "Gogo":
                                barJump()
                        barDebounce = not barDebounce



    scoreContain.draw()
    if difficulty == "Easy":
        easyDifficulty.draw()
        easyText.draw()
    if difficulty == "Normal":
        normalDifficulty.draw()
        normalText.draw()
    if difficulty == "Hard":
        hardDifficulty.draw()
        hardText.draw()
    if difficulty == "Oni":
        oniDifficulty.draw()
        oniText.draw()

    game.drawText(f"{game.score}", drum.left - 30, yPositionLine + 50)
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
    
    if combo > 0:
        game.drawText(f"{combo}", drum.x, yPositionLine)
        comboText.draw()
    
    # for each key, make a sound debounce. when key is pressed, play sound only once. 
    # fix it
    

    for key in debounce_flags:
        if not keys.Pressed[key]:
            if debounce_flags[key]:  # Check if key is released and debounce flag is True
                debounce_flags[key] = False  # Reset debounce flag

    UpdateBulbNotes()
            
            
    game.drawText(f"Drumroll: {getDrumroll()}", 10, game.height - 20)
    game.drawText(f"Max Combo: {maxCombo}", 120, game.height - 20)
    game.drawText(f"Gogo Mode: {getGogoMode()}", 250, game.height - 20)
    game.drawText(f"Bad: {getAccuracy()[0]} Ok: {getAccuracy()[1]} Good: {getAccuracy()[2]}", 10, game.height - 40)

    nextNote = findNextNote(0)
    nextBar = findNextBar(0)

    if songPosition == 0:
        renderNote("bar", None)
    if songPosition >= nextBar:
        renderNote("bar", None)
        findNextBar(1)

    if not nextNote == "EndOfSong":
        if songPosition >= nextNote:
            renderNote(getLastNoteType(), getLastDoDon())
            findNextNote(1)
    else:
        endOfSongTimer += 1
        if endOfSongTimer >= 180:
            game.over = True


    
    songPosition = (time() - startTime)
    frame += 1
    if frame == 60:
        frame = 0
    CheckIfShouldBeHold()
    if health < 0:
        game.over = True
    game.update(60)



game.over = False

while not game.over:
    game.processInput()
    game.clearBackground()
    resultsScreenContainer.draw()

    game.drawText(getAccuracy()[0], 1250, 563)
    game.drawText(getAccuracy()[1], 1250, 627)
    game.drawText(getAccuracy()[2], 1250, 691)
    game.drawText(getDrumroll(), 1620, 580)
    game.drawText(maxCombo, 1660, 675)

    goodText.moveTo(1150, 563)
    okText.moveTo(1150, 627)
    badText.moveTo(1150, 691)

    drumrollText.moveTo(1505, 580)
    maxcomboText.moveTo(1525, 675)


    yellowHealthContainer.moveTo(750, 490)
    greenHealthContainer.moveTo(yellowHealth.x + (greenHealthContainer.width)-5, yellowHealthContainer.y - (greenHealthContainer.height - yellowHealthContainer.height))

    yellowHealth.moveTo(yellowHealthContainer.x + 5, yellowHealthContainer.y+5)

    greenHealth.moveTo(greenHealthContainer.x, greenHealthContainer.y+5)
    yellowHealth.draw()
    greenHealth.draw()

    game.drawText(f"Score: {game.score}", 200, 600)

    reactionText = "congrat"
    game.drawText(f"{reactionText}", 300, 300)

    game.update(60)
game.quit()