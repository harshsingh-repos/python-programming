listOne = [10,9,3,11,2,1]

def sortList(l:list[float])->float:
    for i in range(len(listOne)):
        for j in range(i+1, len(listOne)):
            if (listOne[i]>listOne[j]):
                listOne[j], listOne[i] = listOne[i], listOne[j]
    return listOne

print(sortList(listOne))