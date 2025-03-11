name = "Stella"

# condition if name has charater 'a' print 'a' is present
# for variable in value:
    #executing the block of code
'''
for ch in name:
    print(ch)

for ch in name:
    if ch == 'a':
        print("a is present in name")

'''
#list conatins numbers. Traversing a list of numbers
'''
listNumbers = [1,2,3,4,5,6]

for number in listNumbers:
    print(number)
'''
#Print the charaters which are in upperCase from the variable country
country = "Canada Is A Great Country"
'''
for ch in country:
    if ch.isupper():
        print(ch)
'''
#looping over a certain number of times =>  range()

#Iterating using range, using positive step size and negative step size
'''
for num in range(5):
    print(num)

for num in range(1,5):
    print(num)

for year in range(2000, 2010, 4):
    print(year)

for num in range(5,1,-1):
    print(num)
'''

# variable declaration outside and inside the for loop
# printing the variable outside and inside the for loop
'''
total = 10

for i in range(1, 5):
    total = 10
    total = total + i
    print("Total inside for " , total)

print("Total outside the for " , total)
'''

numbers =[11,22,43,34,15]

# for number in numbers:
#     number = number * 2
#     print(number)

# print(len(numbers))

# for number in range(len(numbers)):
#     number = number * 2
#     print(number)

# for index in range(len(numbers)):
#     print(index, numbers[index])

# for index in range(len(name)):
#     print(index, name[index])

numberListOne = [1,2,3,4,5]
numberListTwo = [6,7,8,9,10]

for outerIndex in range(len(numberListOne)):
    for innerIndex in range(len(numberListTwo)):
        print(numberListOne[outerIndex], numberListTwo[innerIndex])



