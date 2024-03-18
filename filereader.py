bpm = 120
measure = 0
noteIndex = 0
lengthOfMeasure = 5
def findNextNote():
    measureDuration = 1/bpm/60
    noteTimeStamp = measureDuration * measure
    noteTimeStamp += (noteIndex/lengthOfMeasure * measureDuration)