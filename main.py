from gamelib import *

game = Game(1920, 1080, "Taiko no Tatsujin - Python")

outerBar = Image("./images/outerbar.png", game)
innerBar = Image("./images/innerbar.png", game)

outerBar.resizeBy(100)
innerBar.resizeBy(100)
scoreContain = Image("./images/scorecontainer.png", game)

scoreContain.resizeBy(-57)
scoreContain.moveTo(scoreContain.width/2, 153)


drum = Image("./images/taikodrum.png", game)
drumCollide = Image("./images/drumhit.png", game)

drum.resizeBy(-78)


drum.moveTo(scoreContain.width - 100, 153)

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



while not game.over:
    game.processInput()
    game.clearBackground()
    outerBar.draw()
    innerBar.draw()


    scoreContain.draw()
    drum.draw()


    for i in range(len(outerLeftKeys)): # Katsu
        if keys.Pressed[outerLeftKeys[i]]:
            drumOuterLeft.draw()


    for i in range(len(innerLeftKeys)): # Don
        if keys.Pressed[innerLeftKeys[i]]:
            drumInnerLeft.draw()




    game.update(60)
game.quit()