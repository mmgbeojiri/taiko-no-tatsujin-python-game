# Taiko No Tatsujin
A Taiko game recreated in python.

# FAQ
## What songs will be in here?
The starter songs are:
+ Luka Luka Night Fever
+ Meltdown
+ Roki
+ Tokyo Teddy Bear
+ Worlds End Dancehall

## How will the game be played?
Using the keyboard, you can activate the inner and outer sides of the drums.

## What is the song format for songs?
A regular .tja file will suffice.

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
```FileReader.py``` reads the current .tja file and returns the next note's notetype and time stamp.
```Conductor.py``` uses the information from ```FileReader.py``` to add the notes to the render list.
```Notes_N_Classes.py``` are where the actual note code is for, also for bars and drumrolls. 
```Globalvars.py``` are variables that every file can access, mainly for image and text initalizations, but also include some song information.
```Gamelib.py``` is the python game library the project uses.
```Main.py``` deals with the title and selection screen, as well as being the central hub where all files can interact with each other. It renders the UI and also draws everything added to the render list. It also deals with Don Wada himself and the result screen.

## Can I use your assets?
You may, just make sure to credit me in your project.

## Has this stopped development?
There will no longer be daily updates to the game. (5/14/2024)
There may be possible updates where I pick up this game in the future in my free time, but for now, the school project this was made for is due at the time of writing this.
I may come back to this if there is a mainstream reception for this game. Don't be disapointed if this is the last update, as there is a 60% chance I may stop development of this project.
