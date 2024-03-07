from gamelib import *

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

scoreContain = Image("./images/scorecontainer.png", game)

scoreContain.resizeBy(-57)
scoreContain.moveTo(scoreContain.width/2, yPositionLine)


drum = Image("./images/taikodrum.png", game)
drumCollide = Image("./images/drumhit.png", game)

drum.resizeBy(-78)
drumCollide.resizeBy(-78)


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

drumInnerRight.resizeBy(-78)
drumInnerLeft.resizeBy(-78)
drumOuterRight.resizeBy(-78)
drumOuterLeft.resizeBy(-78)

don = Sound("./sounds/Don.wav", 1)
katsu = Sound("./sounds/Katsu.wav", 2)

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
    K_COMMA
]

# Initialize debounce flags for each key
debounce_flags = {
    key: False for key in outerLeftKeys + outerRightKeys + innerLeftKeys + innerRightKeys
}

while not game.over:
    game.processInput()
    game.clearBackground()
    outerBar.draw()
    innerBar.draw()
    drumCollide.draw()

    # Notes #

    scoreContain.draw()
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
            debounce_flags[key] = True  # Set debounce flag to True to prevent multiple plays
            # Play corresponding sound based on key
            if key in innerLeftKeys or key in innerRightKeys:  # Don sound
                don.play()
            else:  # Katsu sound
                katsu.play()
        elif not keys.Pressed[key] and debounce_flags[key]:  # Check if key is released and debounce flag is True
            debounce_flags[key] = False  # Reset debounce flag



    game.update(60)
game.quit()