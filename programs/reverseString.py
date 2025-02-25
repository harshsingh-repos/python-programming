# Program to reverse a string without slicing
string = "This is Python Programming"

def createStringList(string):
    return string.split(" ")  

def reverse(listString):
    reverseStringList = []  
    for element in listString:
        reverseString = ""  
        reverseIndex = len(element) - 1
        while reverseIndex >= 0:
            reverseString += element[reverseIndex]  
            reverseIndex -= 1
        reverseStringList.append(reverseString) 
    return reverseStringList

def reverseString(stringList):
    reversed_sentence = ""  
    index = len(stringList) - 1  
    while index >= 0:
        reversed_sentence += stringList[index] + " "  
        index -= 1
    return reversed_sentence 

splitString = createStringList(string)
print("Original Words List:", splitString)

reversedWordsList = reverse(splitString)
print("Reversed Words List:", reversedWordsList)

finalReversedString = reverseString(reversedWordsList)
print("Final Reversed String:", finalReversedString)
