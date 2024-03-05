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
A dictionary portrayed via numbers in its seperate file that represent beats. it will have a time signature as well. An example:
```
Senbonzakura = {
  "beatsPerMeasure": 8
  "bpm": 150
  "audio": "./sounds/senbonzakura.wav"
  "1": [1,0,1,0,1,0,1,0]
  "2": [1,0,1,0,1,0,1,0]
}
```

Here is the list for the notes.
```
0: No Note
1: Don (red) (middle hit)
2: Katsu (blue) (side hit)
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
 
## How will the engine work?
We will have create functions for the bar, the blue orb, and the red orb.
When a song is loaded, it will read the bpm, and then the time signature.
A beatsPerMeasure of 8 on 150 bpm will mean that, after 8 beats, the bar line will be created.
This will also mean the beatsPerMeasure will make each note an eighth note.
The speed that the lines will be created is dependent on the ```1/(bpm/60)``` forumla.

The music will play offset to the distance of the bar.
When the first bar is sent, and when the song starts, the music will wait unti the first bar reaches the start of the drum, and then start.

## Can I use your assets?
yea
just credit
pelase
i mean im not going to go after you but it will hurt mi feeling :C
