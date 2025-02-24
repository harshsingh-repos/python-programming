listOne = [2,3,4,1,5,6,7,9]
listTwo = [2,4,6,7,10,11]
mergeList = listOne.copy() #shallow copy

def mergeListsWithoutDuplicates(listOne, listTwo):
    for j in range(len(listTwo)):
        if listTwo[j] not in listOne:
            mergeList.append(listTwo[j])
    
    print(mergeList) #mergedList
    print(listOne) #not changing listOne
    print(listTwo) #not changing listTwo


mergeListsWithoutDuplicates(listOne,listTwo)