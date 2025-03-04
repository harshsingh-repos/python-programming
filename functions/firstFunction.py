#What is a function ? - a specific task
# reuse code, break programs into smaller pieces, more readable
# efficent

def greet():
    print("Hello Welcome to Functions")


# calling the function
# greet() 

#function with single parameter 
# function have parameter default to "User"
def greet_user(name="User"): #using parameters in the function body 
    print(f"Hello {name}, welcome to this function session")


# name = "Justice"
# greet_user("John") #passing agruments in the function call
# greet_user("Bob")
# greet_user("Stella")
# greet_user("Singh")
# greet_user(name)

greet_user()

greet_user("Manni")
