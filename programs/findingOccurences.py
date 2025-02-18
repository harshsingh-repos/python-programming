# Python program to find occurences of charaters in string
string = "This is python programming"

occurrenceDict = {}
def countOccurreces():
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

print(countOccurreces())