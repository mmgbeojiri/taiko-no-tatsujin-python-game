# Taiko No Tatsujin
A Taiko game recreated in python.

# FAQ
## What songs will be in here?
Most likely that this will not be a lot of songs, however I was thinking about some. The only ones I could think of are
+ SEKAI-chan to KAFU-chan no Otsukai Gassoukyoku
+ Senbonzakura

## How will the game be played?
Using the keyboard, you can activate the inner and outer sides of the drums.

## What is the song format for songs?
A dictionary portrayed via numbers that represent beats. it will have a time signature as well. An example:
```
Senbonzakura = {
  "timeSigNumer": 4
  "timeSigDeno": 8
  "audio": "./sounds/senbonzakura.wav"
  "1": [1,0,1,0,1,0,1,0]
  "2": [1,0,1,0,1,0,1,0]
}
```

## What will be the design?
A more modern minimalistic design.

## Why did you make this?
Because I have been fascinated by the gameplay of Taiko No Tatsujin, however I dont have a Nintendo Switch. Also because this is a school project.

## What are the hotkeys?
+ 1, 2, 3, 4, 5, q, w, e, r, t
  + Outer Left Drum (Blue)
+ 6, 7, 8, 9, 0, y, u, i, o, p
  + Outer Right Drum (Blue)
+ a, s, d, f, g, z, x, c, v, b
  + Inner Left Drum (Red)
+ h, j, k, l, ;, n, m, ",", ".", "/"
  + Inner Right Drum (Red)
