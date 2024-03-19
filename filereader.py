measure = 0
noteIndex = 0
lengthOfMeasure = 5
song = "Luka Luka Night Fever"

tjaFile = f"./tjadatabase/{song}/{song}.tja"

def findNextNote():
    global bpm, measure, noteIndex
    
    songFile = open(tjaFile, "r")
    for i, value in enumerate(songFile)
    beatMapLine = songFile
              
              measure = i-startSongLine
              measureDuration = 1/bpm/60
              noteTimeStamp = measureDuration * measure
              noteTimeStamp += (noteIndex/lengthOfMeasure * measureDuration)

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

        