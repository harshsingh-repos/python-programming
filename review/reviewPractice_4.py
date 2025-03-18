#Get an input of positive numbers from user, (negative input will end the program). 
#Add the positive numbers
#display the highest number
#display the lowest number

number = int(input("Enter a number (negative to exit): ")) # 10 , 8
total = 0
maximum = number #10 , 8
minimum = number #10 , 8 
while number >=0:
    total = total + number  #10 , 18
    
    if number > maximum:  # 2 input max is still 10
        maximum = number

    if number < minimum: # 2 input min is less than 10
        minimum = number

    number = int(input("Enter a number (negative to exit): "))

print("Total of the numbers: " , total)
print("The highest number was: ", maximum)
print("The lowest number was: ", minimum)
    