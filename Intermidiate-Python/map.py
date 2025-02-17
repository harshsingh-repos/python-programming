fruits = ["apple", "orange", "banana", "watermelon"]

def listFruits():
    for fruit in fruits:
        print(fruit)
    
def getFruitLength(fruit):
    return len(fruit)
    
newFruitList =[]
newNumberList =[]

def fruitLengthGreaterThanSix():
    for fruit in fruits:
        if getFruitLength(fruit) >= 6:
            newFruitList.append(fruit)
    print(newFruitList)


def numberList():
    for fruit in fruits:
        newNumberList.append(len(fruit))
    
    return newNumberList

# listFruits()
# fruitLengthGreaterThanSix()

# print(numberList())
# combining all the requirement for numberlist using map
# print(list(map(getFruitLength, fruits))) 
# combining all the requirement for numberlist in list comprehension
# print([getFruitLength(fruit) for fruit in fruits])

print([getFruitLength(fruit) for fruit in fruits if getFruitLength(fruit) >=6])