# Python program to find occurences of charaters in string
# inputString = "This is python programming"

inputString = "This is a test"

occurrenceDict = {}
def countOccurreces(string):
    stringList = []
    for ch in string:
        stringList.append(ch.lower())
    index = len(stringList)
    for i in range(index):
        if stringList[i] not in occurrenceDict:
            count = 0
            for j in range(index):
                if(stringList[i] == stringList[j]):
                    count +=1
            occurrenceDict.update({stringList[i]: count})
    return occurrenceDict

print(countOccurreces(inputString))