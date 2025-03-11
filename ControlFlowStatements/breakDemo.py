# program to break if the user enters exit or quit

while True:
    text = input("Enter a string or 'quit' to exit : ")
    if text == 'quit':
        print("Exiting the program")
        break
    elif len(text) == 0:
        print("I missed the input, enter the string again")
    elif len(text) > 0:
        print("You have entered: ", text)