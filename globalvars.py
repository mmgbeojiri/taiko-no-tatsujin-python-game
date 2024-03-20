from gamelib import *
from time import *

game = Game(1920, 1080, "Taiko no Tatsujin - Python")

yPositionLine = 153
drumResize = -78

scrollSpeed = 10
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
effect = Image("./images/effect.png", game)
effect.resizeTo(5, 5)

drumInnerRight.resizeBy(drumResize)
drumInnerLeft.resizeBy(drumResize)
drumOuterRight.resizeBy(drumResize)
drumOuterLeft.resizeBy(drumResize)

don = Sound("./sounds/Don.wav", 1)
katsu = Sound("./sounds/Katsu.wav", 2)


barMultipler = 9
yellowHealth = Shape("bar", game, 50 * barMultipler, 20, yellow)
greenHealth = Shape("bar", game, 50 * barMultipler, 20, green)

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
    K_PERIOD,
    K_SLASH
]

# Initialize debounce flags for each key
debounce_flags = {
    key: False for key in outerLeftKeys + outerRightKeys + innerLeftKeys + innerRightKeys
}


