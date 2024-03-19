bpm = 120
measure = 0
noteIndex = 0
lengthOfMeasure = 5
song = "Luka Luka Night Fever"

tjaFile = f"./tjadatabase/{song}/{song}.tja"
def findNextNote():
    measureDuration = 1/bpm/60
    noteTimeStamp = measureDuration * measure
    noteTimeStamp += (noteIndex/lengthOfMeasure * measureDuration)

def FindLineWith(filename, string):
  """
  This function finds lines in an external file that contain the specified string.

  Args:
      filename: The name of the file to search.
      string: The string to find.

  Returns:
      A list of strings, where each string is the value after the target string, followed by the line number.
  """

  results = []
  with open(filename, "r") as file:
    for i, line in enumerate(file):
      if string in line:
        value = line.split(string)[1].strip()  # Extract value after the string
        results.append(f"{value},{i}")  # Append value and line number to results
  return results
