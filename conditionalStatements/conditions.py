# Conditional Statements : process some logic
# Conditional Execution: A block of one or more Statements which will be executed if a certian expression is true
# Repetetive Execution: A block of one or more Statements that will be Repetetetively executed as long as the expresion is true


# if condition:
#     this part of code will run for true condition only

num = 10
# if num > 0:
#     print("The number is positive") #the block/statement will execute when num > 10 => True

# if num < 10:
#     print(f"The number {num} is less or equal to 10")

# if num == 10:  #    = (assignment operator) , == (equality operator)
#     print(f"The number is equal to {num}") #statement will execute if the number is exactly 10

# if num < 10:
#     print(f"The number {num} is less than 10")
# else:
#     print(f"The number {num} is not less than 10")

# num = 7
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

num = 0
if num < 0 :
    print("The number is negative")
elif num > 0:
    print("The number is positive")
else:
    print("The number is zero")

num = 10
if (num<100) and (num>0):
    print("The number is between 0 and 100")
elif (num<0):
    print("The number is negative")
else:
    print("The number is zero")