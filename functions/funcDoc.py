# documentation is a key

def add(numberOne: int , numberTwo: int)-> int:
    """
    This function will return the sum of two numbers
    @param1 : int 
    @param2 : int
    @return : int

    >>> add(2,3) 
    5
    """
    return numberOne+numberTwo

# print(add(2,3))
# print(add(2, "singh")) #typeError
print(add(-2, -10))
print(add("Bob", "Marley"))
