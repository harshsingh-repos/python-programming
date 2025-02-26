listOne = [1,2,3,2,3,4,1,2]
list_one = [1, 2, 2, 3, 4, 4, 5]


def removeDuplicates(l):
    uniqueList =[]
    for item in l:
        if item not in uniqueList:
            uniqueList.append(item)
    return uniqueList


def removeDups(l):
    uniqueList = l.copy()
    length = len(l)
    for i in range(length):
        for j in range(i+1, length):
            if(l[i]==l[j]):
                uniqueList.pop(l[i])      
    return uniqueList

# print(removeDuplicates(listOne))
print(removeDups(list_one))
            