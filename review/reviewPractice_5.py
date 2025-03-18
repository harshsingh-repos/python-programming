# find if the number is prime

def findPrime(number):
    if number <=1:
        return False

    for index in range(2, number):
        if(number % index == 0):
            return False
    
    return True

number = int(input("Enter a positive integer (negative to exit): "))
while number >=0:
    if(findPrime(number)):
        print( number , "is a prime number")
    else:
        print(number, "is not a prime number")
    number = int(input("Enter a positive integer (negative to exit): "))

