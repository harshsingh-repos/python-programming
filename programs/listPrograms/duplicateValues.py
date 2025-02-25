#finding duplicate values in a list

import time
# fruits = ["Apple", "Orange", "Banana", "Apple", "Orange", "Watermelon"]

numbers = [1,2,3,4,3,2,1,4,6,7,2]

def findDuplicateValues(inputList):
    duplicateValuesInList =[]
    index = len(inputList)
    for i in range(index):
        if inputList[i] not in duplicateValuesInList:
            count =1
        for j in range(i+1, index):
            if (inputList[i] == inputList[j]):
                count +=1
                if inputList[i] in duplicateValuesInList:
                    continue
                else:
                    duplicateValuesInList.append(inputList[i])

    return duplicateValuesInList


# print(findDuplicateValues(fruits))
# print(findDuplicateValues(numbers))

assert findDuplicateValues([1, 2, 3, 4, 3, 2, 1, 4, 6, 7, 2]) == [1, 2, 3, 4], "Test Case 1 Failed"
assert findDuplicateValues([5, 10, 5, 10, 5, 10]) == [5, 10], "Test Case 2 Failed"
assert findDuplicateValues([1, 2, 3, 4, 5]) == [], "Test Case 3 Failed"  # No duplicates
assert findDuplicateValues([]) == [], "Test Case 4 Failed"  # Empty list
assert findDuplicateValues([100, 200, 300, 100, 300, 400]) == [100, 300], "Test Case 5 Failed"
assert findDuplicateValues(["a", "b", "c", "a", "c", "d"]) == ["a", "c"], "Test Case 6 Failed"  # Works for strings
assert findDuplicateValues(["x", "y", "z", "x", "y", "y", "z", "z"]) == ["x", "y", "z"], "Test Case 7 Failed"
assert findDuplicateValues([1, 1, 1, 1, 1]) == [1], "Test Case 8 Failed"  # All same elements
assert findDuplicateValues([10, 20, 30, 40, 50, 60]) == [], "Test Case 9 Failed"  # No duplicates
assert findDuplicateValues([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [2, 3, 4], "Test Case 10 Failed"

print("✅ All test cases passed!")