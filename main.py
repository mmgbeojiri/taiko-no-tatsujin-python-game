from random import randint
from gamelib import *
from globalvars import * # All the Global Variables (Defining the inital keys and sprites)
from notes_n_classes import * # All the Note Types and Classes (available for cloning)
from filereader import * # responsible for reading the chart
from conductor import * # responsible for rendering notes from the filereaders

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

blueTransparentImage = pygame.image.load("./images/blue.png").convert()
redTransparentImage = pygame.image.load("./images/red.png").convert()
def UpdateBulbNotes():
    global blueTransparentImage, redTransparentImage
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
    if getHoldStatus() == True and frame % 4 == 0:
        createObject("holdmiddle")

while not game.over:
    game.processInput()
    game.clearBackground()
    outerBar.draw()
    health = getHealth()
    combo = getCombo()
    if health < 50:
        yellowHealth.width = health * barMultipler
    else:
        yellowHealth.width = 50 * barMultipler

    if health > 50:
        greenHealth.width = health/2 * barMultipler
    else:
        greenHealth.width = 0


    yellowHealthContainer.moveTo(0, scoreContain.top-(yellowHealthContainer.height/2))
    greenHealthContainer.moveTo(yellowHealth.x + (50*barMultipler), yellowHealthContainer.y - (greenHealthContainer.height - yellowHealthContainer.height))

    yellowHealth.moveTo(yellowHealthContainer.x + 5, yellowHealthContainer.y+5)

    greenHealth.moveTo(greenHealthContainer.x, greenHealthContainer.y+5)
    yellowHealth.draw()
    greenHealth.draw()

    innerBar.draw()
    effect.draw()
    effect.resizeBy(-2)
    effect.moveTo(drumCollide.x, drumCollide.y)
    drumCollide.draw()

    
    

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

    UpdateBulbNotes()
            
            


    if songPosition == 0:
        renderNote("bar")
    if songPosition >= findNextBar(0):
        renderNote("bar")
        findNextBar(1)

    if songPosition >= findNextNote(0):
        renderNote(getLastNoteType())
        findNextNote(1)

    
    songPosition = (time() - startTime)
    frame += 1
    if frame == 60:
        frame = 0
    CheckIfShouldBeHold()
    if health < 0:
        game.over = True
    game.update(60)
game.quit()