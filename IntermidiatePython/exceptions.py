#exceptions

def divide(numOne, numTwo):
    try:
        return numOne/numTwo
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print(f"Error:{e} ") 

divide(10,0)
print(divide(10,2))
divide("a", 10)