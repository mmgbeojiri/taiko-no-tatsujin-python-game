from globalvars import *
measure = 0
measureWithComments = 0
noteIndex = 0
barIndex = 0
noteTimeStamp = 0
barTimeStamp = 0
noteType = "0"
noOffset = True
gogoMode = False
doDon = None


tjaFile = f"./tjadatabase/{song}/{song}.tja"
def getLastNoteTimeStamp():
  return noteTimeStamp
def getLastDoDon():
  return doDon
def getGogoMode():
   return gogoMode

def getLastNoteType():
   return str(noteType)

def FindStartEndSongLine(endOrStart, diffuculty):
   global startSongLine, endSongLine
   diffucultyLine = FindLineWith(f"COURSE:{diffuculty}", "Number") #line of diffuculty.
   if endOrStart == "Start":
    return FindLineWith("#START", "Number", diffucultyLine)
   elif endOrStart == "End":
    return FindLineWith("#END", "Number", diffucultyLine)
   else:
      return 0



def findNextBar(updateBarIndex = 1):
    global bpm, barIndex, measureDuration, offset
    barTimeStamp = barIndex * measureDuration
    barTimeStamp += offset
    if updateBarIndex:
      barIndex += 1
    return barTimeStamp
    


def findNextNote(updateNoteIndex = 1):
    global bpm, measure, noteIndex, measureWithComments, noteTimeStamp, noteType, measureDuration, offset, gogoMode, doDon


             
    songFile = open(tjaFile, "r")
    for lineNumber, lineString in enumerate(songFile):
      if lineNumber == startSongLine + measureWithComments: # Check if this is the line we want to check
        if lineNumber >= (endSongLine):
             return "EndOfSong"
        beatMapLine = lineString
        noteType = beatMapLine[noteIndex]
        lengthOfMeasure = len(beatMapLine.split(',')[0])
        if lengthOfMeasure == 0:
          lengthOfMeasure = 1
        noteTimeStamp = measureDuration * (measure)
        noteTimeStamp += (noteIndex/lengthOfMeasure) * measureDuration
        noteTimeStamp += offset
        if beatMapLine[noteIndex] == ",": # check if this is new line
            measure += 1
            measureWithComments += 1
            noteIndex = 0
            continue
        try: #check if this is a number
          val = int(beatMapLine[noteIndex])
        except ValueError:
          print("That's not an int!")
          print(f"noteType {noteType}")
          measureWithComments += 1
          if str(beatMapLine) == "#GOGOSTART\n":
             print("gogostart")
             gogoMode = True
          if str(beatMapLine) == "#GOGOEND\n":
             print("gogoend")
             gogoMode = False
          
          continue
        if noteType == "1":
          if "0" in str(beatMapLine[noteIndex+1]):
              doDon = "Don"
          elif "," in str(beatMapLine[noteIndex+1]):
              doDon = "Don"
          else:
              doDon = "Do"
        elif noteType == 3:
              doDon = "Don"
        else:
          doDon = None
        print(f"measure: {measure} noteindex: {noteIndex} read from {lineNumber} noteType {noteType} noteTimeStamp: {noteTimeStamp} doDon: {doDon}")
        if updateNoteIndex:
          noteIndex += 1
        return noteTimeStamp # end the function
      else: # Skip the line if its not ours
           continue


def FindLineWith(string, StringOrNum, lineNumberOffset = 0):
  global tjaFile
  """
  This function finds lines in an external file that contain the specified string.

  Args:
      filename: The name of the file to search.
      string: The string to find.

  Returns:
      A list of strings, where each string is the value after the target string, followed by the line number.
  """

  results = []
  
  with open(tjaFile, "r") as file:
    for i, line in enumerate(file):
      if i < lineNumberOffset: #If the I is less than the line number, then skip over
         continue 
      if string in line:
        value = line.split(string)[1].strip()  # Extract value after the string
        if StringOrNum == "String":
            return str(value)
        else:
            return i  # Append value and line number to results
  return 0 #if there is no line

title = FindLineWith("TITLE:", "String")
subtitle = FindLineWith("SUBTITLE:", "String")
bpm = FindLineWith("BPM:", "String")
wave = FindLineWith("WAVE:", "String")
startSongLine = 0
endSongLine = 0
def onDifficultyChange(difficulty):
  startSongLine = FindStartEndSongLine("Start", difficulty)
  endSongLine = FindStartEndSongLine("End", difficulty)

measureDuration = (60/int(bpm))*4
offset = float(FindLineWith("OFFSET:", "String"))
if noOffset:
   offset = 0
def getSoundFile():
    return f"./tjadatabase/{song}/{wave}"



        