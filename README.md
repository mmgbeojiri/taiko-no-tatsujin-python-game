# Taiko No Tatsujin
A Taiko game recreated in python.

# FAQ
## What songs will be in here?
Most likely that this will not be a lot of songs, however I was thinking about some. The only ones I could think of are
+ SEKAI-chan to KAFU-chan no Otsukai Gassoukyoku
+ Senbonzakura
+ Bad Apple
+ Rin-Chan Now!

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
    + Note: the period and slash key don't work.
 
## How will the engine work?
We will have create functions to create the bar, the blue orb, and the red orb.
The scroll speed will be set to 10.
There are two main functions that will control the song.

The ```FindNextNote()``` function will find the timestamp of the next note, and the notetype. This is how it'll work.
--
```
measureLength = 1/bpm/60
noteTimeStamp = measureLength * measure
noteTimeStamp += (noteIndex/lengthOfMeasure * measureLength)
```
The measure length is equal to 1 / bpm / 60. For example, if the BPM is 120, ```measureLength``` will be 0.5.
Then, the noteTimeStamp will be calculated. Here is a example of the .tja file we will use.

```
#START
10201020,
20102010,
#END
```
The ```measure``` is equal to the line number we are reading relative to the ```#START``` minus 1. 
So if we were on the first line, ```measure``` would be equal to 0.
The ```measureLength``` is the length of the measure, this is 8 and will change for each line.
If we are doing the first note, ```then noteIndex``` would be equal to 0.

So, to get the timestamp of the first note, we would do
```
measureLength = 1/120/60 # 0.5
noteTimeStamp = 8 * 0 # 0
noteTimeStamp += (0/8 * 0.5) # 0
```
So noteTimeStamp would be zero.

So, to get the timestamp of the second note, we would do
```
measureLength = 1/120/60 # 0.5
noteTimeStamp = 8 * 0 # 0
noteTimeStamp += (1/8 * 0.5) # 0.0625
```
So noteTimeStamp would be 0.0625.

There will also be a ```barTimeStamp``` to caluclate the next bar,  using only the ```measureLength * measure``` formula.
```noteType`` will be set to the line of the measure, and indexed by noteIndex.
Then, the values will be passed to the next functions,
```
WaitToRenderNote(noteType, noteTimeStamp)
WaitToRenderBar(barTimeStamp)
```
FindNextNote() will be ran every frame.

WaitToRenderNote(noteType, noteTimeStamp) will wait until the songPosition reaches the noteTimeStamp to add a note to the Render list.
--
```
if songPosition > noteTimeStamp:
  if noteType == "1"
    render.append(Blue())
```
After songPosition is greater, it will run ```FindNextNote()``` again to avoid duplicates.

WaitToRenderBar(barTimeStamp) will wait until songPosition reaches the barTimeStamp to add a bar to the Render List
--
```
if songPosition > barTimeStamp:
  render.append(Bar())
```
WaitToRenderBar() will not run ```FindNextNote()``` again.

CheckForHit() will check if how close the notes are to being on the rhythm line when hit. This is ran in the note Classes.
--
A special varible called ```SongStartDebounce``` will be used during the CheckForHit function for the Bar

```
SongStartDebounce = True
if self.x < drum.collide.x:
  if SongStartDebounce:
    playMusic()
```
Detects when the first bar reaches the drum, it'll start to play the music, and the following bars won't.

The music will play offset to the distance of the bar.
When the first bar is sent, and when the song starts, the music will wait unti the first bar reaches the start of the drum, and then start.

## Can I use your assets?
yea
just credit
pelase
i mean im not going to go after you but it will hurt mi feeling :C
