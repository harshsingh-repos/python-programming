#scope of a variable - Where can it be used

varX = 10 #global variable

def modify():
    global varX #global keyword to change the value of a global variable inside the function
    varX = 5 #local to the function
    print("Inside the function: ",varX)

modify()
print("Outside the function: ", varX)

