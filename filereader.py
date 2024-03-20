measure = 0
noteIndex = 0
lengthOfMeasure = 5
song = "Luka Luka Night Fever"

tjaFile = f"./tjadatabase/{song}/{song}.tja"

def findNextNote():
    global bpm, measure, noteIndex

    songFile = open(tjaFile, "r")
    for lineNumber, lineString in enumerate(songFile):
      if lineNumber == startSongLine + measure + 1: # Check if this is the line we want to check
        beatMapLine = lineString
        for noteIndexCheck, letter in enumerate(beatMapLine): #
          if noteIndex == noteIndexCheck:
              noteType = letter
              measureDuration = 1/int(bpm)/60
              noteTimeStamp = measureDuration * measure
              noteTimeStamp += (noteIndex/lengthOfMeasure * measureDuration)
              print(f"measure: {measure}")
              print(f"noteindex: {noteIndex}")
              print(f"read from {i}")
              print(f"noteType {noteType}")
              noteIndex += 1
              break
          if letter == ",": #new line
              measure += 1
              noteIndex = 0
              break
          try:
            val = int(letter)
          except ValueError:
            print("That's not an int!")
            continue
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

        