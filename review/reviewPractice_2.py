# Read a list of names from keyboard input and display then in uppercase on the scree as they are read in.
# Conitnue reading until the user enter a 'STOP' to end the set of enteries. 
# After all names have been processed, print a message and a count of the names that were printed. 

#1. Read input - display in uppercase -- use input
#2. STOP when user enters STOP -- this is a condition -- use while loop
#3. Count the names -- use variable count
#4. Print a message

'''
count = 0
name =""
while name!= 'STOP':
    name = input("Please enter a name (STOP to exit): ").upper()
    if(name !="STOP"):
        print("Name:" , name)
        count +=1

        print("User entered ", count , "names.")
'''
count = 0
name = input("Please enter a name (STOP to exit): ").upper()
while name!= 'STOP':
    print("Name:" , name)
    count +=1
    name = input("Please enter a name (STOP to exit): ").upper()

print("User entered ", count , "names.")