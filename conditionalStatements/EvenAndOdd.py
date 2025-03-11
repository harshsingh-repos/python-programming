# num = int(input("Enter the number: "))
# if num > 0:
#     if num % 2 == 0:
#         print("The number is positive and even integer")
#     else: 
#         print("The number is positive and odd")
# elif num == 0:
#     print("The number is zero")
# else: 
#     print("The number is negative")

def evenAndOdd(num):
    if num > 0:
        if num % 2 == 0:
            print(f"The number {num} is positive and even integer")
        else: 
            print(f"The number {num} is positive and odd")
    elif num == 0:
        print(f"The number {num} is zero")
    else: 
        print(f"The number {num} is negative")

evenAndOdd(-10)
evenAndOdd(10)
evenAndOdd(0)
evenAndOdd(7)

