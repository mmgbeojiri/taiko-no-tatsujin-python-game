from gamelib import *
from time import *

game = Game(1920, 1080, "Taiko no Tatsujin - Python")

yPositionLine = 153
drumResize = -78

scrollSpeed = 15
drumHitboxAdd = 5



outerBar = Image("./images/outerbar.png", game)
innerBar = Image("./images/innerbar.png", game)

outerBar.resizeBy(100)
innerBar.resizeBy(100)



scoreContain = Image("./images/scorecontainer.png", game)

scoreContain.resizeBy(-57)
scoreContain.moveTo(scoreContain.width/2, yPositionLine)


drum = Image("./images/taikodrum.png", game)
drumCollide = Image("./images/drumhit.png", game)
drumCollide.resizeBy(drumResize)
drum.resizeBy(drumResize)


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
okEffect = Image("./images/effect.png", game)
badEffect = Image("./images/badEffect.png", game)
goodEffect = Image("./images/goodEffect.png", game)
badEffect.resizeTo(5, 5)
goodEffect.resizeTo(5, 5)
okEffect.resizeTo(5, 5)

drumInnerRight.resizeBy(drumResize)
drumInnerLeft.resizeBy(drumResize)
drumOuterRight.resizeBy(drumResize)
drumOuterLeft.resizeBy(drumResize)

don = Sound("./sounds/Don.wav", 1)
katsu = Sound("./sounds/Katsu.wav", 2)

maxCombo = 0

barMultipler = 9
yellowHealth = Shape("bar", game, 75 * barMultipler, 20, yellow)
greenHealth = Shape("bar", game, 50 * barMultipler, 25, green)

yellowHealthContainer = Shape("bar", game, 75 * barMultipler+5, yellowHealth.height+10, (51, 51, 17))
greenHealthContainer = Shape("bar", game, 50 * barMultipler+5, greenHealth.height+10, (17, 51, 17))


bulbx = greenHealthContainer.right
bulby = greenHealthContainer.top-(greenHealthContainer.height/2)

easyDifficulty = Image("./images/easyDif.png", game)
normalDifficulty = Image("./images/normalDif.png", game)
hardDifficulty = Image("./images/hardDif.png", game)
oniDifficulty = Image("./images/oniDif.png", game)

easyDifficulty.resizeBy(drumResize)
normalDifficulty.resizeBy(drumResize)
hardDifficulty.resizeBy(drumResize)
oniDifficulty.resizeBy(drumResize)

easyDifficulty.moveTo(scoreContain.x - 100, scoreContain.y)
normalDifficulty.moveTo(scoreContain.x - 100, scoreContain.y)
hardDifficulty.moveTo(scoreContain.x - 100, scoreContain.y)
oniDifficulty.moveTo(scoreContain.x - 100, scoreContain.y)

easyText = Image("./text/easy.png", game)
normalText = Image("./text/normal.png", game)
hardText = Image("./text/hard.png", game)
oniText = Image("./text/oni.png", game)

easyText.resizeBy(drumResize)
normalText.resizeBy(drumResize)
hardText.resizeBy(drumResize)
oniText.resizeBy(drumResize)

easyText.moveTo(scoreContain.x - 100, scoreContain.y+50)
normalText.moveTo(scoreContain.x - 100, scoreContain.y+50)
hardText.moveTo(scoreContain.x - 100, scoreContain.y+50)
oniText.moveTo(scoreContain.x - 100, scoreContain.y+50)

comboText = Image("./text/combo.png", game)
comboText.resizeBy(drumResize-5)
comboText.moveTo(drum.x, yPositionLine+40)

def hitEffect(type = "ok"):
    global drumCollide, okEffect, badEffect, goodEffect
    if type == "good":
        goodEffect.resizeTo(78, 78)
        goodEffect.resizeBy(130)
    elif type == "bad":
        badEffect.resizeTo(78, 78)
        badEffect.resizeBy(130)
    else:
        okEffect.resizeTo(78, 78)
        okEffect.resizeBy(130)


endOfSongTimer = 0

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
    K_PERIOD,
    K_SLASH
]

# Initialize debounce flags for each key
debounce_flags = {
    key: False for key in outerLeftKeys + outerRightKeys + innerLeftKeys + innerRightKeys
}

resultsScreenContainer = Image("./images/results.png", game)
resultsScreenContainer.resizeTo(game.width, game.height)

goodText = Image("./text/good.png", game)
okText = Image("./text/ok.png", game)
badText = Image("./text/bad.png", game)

drumrollText = Image("./text/drumrollresult.png", game)
maxcomboText = Image("./text/maxcombo.png", game)

goodText.resizeBy(drumResize+5)
okText.resizeBy(drumResize+5)
badText.resizeBy(drumResize+5)

drumrollText.resizeBy(drumResize+5)
maxcomboText.resizeBy(drumResize+5)

logo = Image("./images/logo.png", game)
clickAnywhere = Image("./text/clickanywhere.png", game)
selectedSong = Image("./text/selectedsong.png", game)

logo.resizeBy(50)
selectedSong.resizeBy(-50)

clickAnywhere.moveTo(game.width/2, (game.height/4)*3)
selectedSong.moveTo(300, 40)

startEasyDifficulty = Image("./images/easyDif.png", game)
startNormalDifficulty = Image("./images/normalDif.png", game)
startHardDifficulty = Image("./images/hardDif.png", game)
startOniDifficulty = Image("./images/oniDif.png", game)

startEasyDifficulty.resizeBy(drumResize)
startNormalDifficulty.resizeBy(drumResize)
startHardDifficulty.resizeBy(drumResize)
startOniDifficulty.resizeBy(drumResize)

startEasyDifficulty.moveTo(240, game.height/2)
startNormalDifficulty.moveTo(720, game.height/2)
startHardDifficulty.moveTo(1200, game.height/2)
startOniDifficulty.moveTo(1680, game.height/2)

startEasyText = Image("./text/easy.png", game)
startNormalText = Image("./text/normal.png", game)
startHardText = Image("./text/hard.png", game)
startOniText = Image("./text/oni.png", game)

startEasyText.resizeBy(drumResize)
startNormalText.resizeBy(drumResize)
startHardText.resizeBy(drumResize)
startOniText.resizeBy(drumResize)

startEasyText.moveTo(startEasyDifficulty.x, startEasyDifficulty.y + 50)
startNormalText.moveTo(startNormalDifficulty.x, startEasyDifficulty.y + 50)
startHardText.moveTo(startHardDifficulty.x, startEasyDifficulty.y + 50)
startOniText.moveTo(startOniDifficulty.x, startOniDifficulty.y + 50)

difficulty = "Hard"
song = "Luka Luka Night Fever"