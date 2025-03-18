#Print the numbers 1 to 10 and the sqaure of each
#Print the numbers 10 to 21 and the sqaure of each -- range(10,22)

'''
for number in range(1,11):
    square = number * number
    print("Number = " ,  number , "Square: " , square)


number = 10
while number <=21:
    square = number * number
    print("Number = ", number , "Sqaure: ", square)
    number +=1
    '''

#Sum all the even numbers from 2, 31, printing the number and a running total as it accumulates

'''
total = 0
number = 2
while number <=31:
    total = total + number  #total += number
    print("number : " , number , "running total= " , total)
    number +=2
'''
total = 0
for number in range(2,32):
    if(number%2 == 0):
        total = total + number
        print("number : " , number , "running total= " , total)
