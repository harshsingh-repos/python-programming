#combining two unequal length lists. 

listOne = [1,2,3,4]
listTwo = [5,6,7,8,9,10]


def combine(listOne,listTwo):
    combinedList = []
    lenA, lenB = len(listOne), len(listTwo)
    minLength = min(lenA, lenB)

    for i in range(minLength):
        combinedList.append(listOne[i])
        combinedList.append(listTwo[i])
    
    if is_longer(listOne, listTwo) == True:
        combinedList.extend(listOne[minLength:])
    else:
        combinedList.extend(listTwo[minLength:])

    return combinedList


def is_longer(l1: list, l2: list) -> bool:
    if(len(l1)> len(l2)):
        return True
    else:
        return False

# print(is_longer(listOne,listTwo))
print(combine(listOne,listTwo))