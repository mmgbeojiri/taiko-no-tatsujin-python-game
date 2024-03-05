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

drum.resizeBy(-)
drum.moveTo(scoreContain.width/2, 153)

blue = Image("./images/blue.png", game)
red = Image("./images/red.png", game)
effect = Image("./images/effect.png", game)

while not game.over:
    game.processInput()
    outerBar.draw()
    innerBar.draw()

    scoreContain.draw()
    drum.draw() 
    game.update(60)
game.quit()
