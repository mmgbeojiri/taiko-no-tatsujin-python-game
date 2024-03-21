measure = 0
measureWithComments = 0
noteIndex = 0
barIndex = 0
noteTimeStamp = 0
barTimeStamp = 0
noteType = "0"
song = "Luka Luka Night Fever"

tjaFile = f"./tjadatabase/{song}/{song}.tja"
def getLastNoteTimeStamp():
  return noteTimeStamp

def getLastNoteType():
   return str(noteType)


def findNextBar(updateBarIndex = 1):
    global bpm, barIndex
    measureDuration = 1/2*int(bpm)/60
    barTimeStamp = barIndex * measureDuration
    print(barTimeStamp)
    if updateBarIndex:
      barIndex += 1
    return barTimeStamp
    


def findNextNote(updateNoteIndex = 1):
    global bpm, measure, noteIndex, measureWithComments, noteTimeStamp, noteType

    songFile = open(tjaFile, "r")
    for lineNumber, lineString in enumerate(songFile):
      if lineNumber == startSongLine + measureWithComments: # Check if this is the line we want to check
        beatMapLine = lineString
        for noteIndexCheck, letter in enumerate(beatMapLine): # Enumeratre through the line
          if noteIndex == noteIndexCheck: #If this is our number
              noteType = letter
              lengthOfMeasure = len(beatMapLine)
              measureDuration = 1/4*int(bpm)/60
              noteTimeStamp = measureDuration * measure
              noteTimeStamp += (noteIndex/lengthOfMeasure) * measureDuration -(1/lengthOfMeasure)
              if letter == ",": # check if this is new line
                  measure += 1
                  measureWithComments += 1
                  noteIndex = 0
                  break
              try: #check if this is a number
                val = int(letter)
              except ValueError:
                print("That's not an int!")
                print(f"noteType {noteType}")
                measureWithComments += 1
                break
              print(f"measure: {measure} noteindex: {noteIndex} read from {lineNumber} noteType {noteType} noteTimeStamp: {noteTimeStamp}")

              if updateNoteIndex:
                noteIndex += 1
              return noteTimeStamp # end the function
      else: # Skip the line if its not ours
           continue


def FindLineWith(string, StringOrNum):
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
      if string in line:
        value = line.split(string)[1].strip()  # Extract value after the string
        if StringOrNum == "String":
            return str(value)
        else:
            return i  # Append value and line number to results
  return results

title = FindLineWith("TITLE:", "String")
subtitle = FindLineWith("SUBTITLE:", "String")
bpm = FindLineWith("BPM:", "String")
wave = FindLineWith("WAVE:", "String")
startSongLine = FindLineWith("#START", "Number")
endSongLine = FindLineWith("#END", "Number")

print(title)
print(subtitle)
print(bpm)
print(wave)
print(startSongLine)
print(endSongLine)

        