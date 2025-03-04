#Multiple parameters and return value

def add(numOne, numTwo):
    sum = numOne + numTwo
    return sum
    
# result = add(2,3)
# print(result)
# print(add(2,3))

def calculate(numOne, numTwo):
    return numOne+numTwo , numOne-numTwo

sum_val, diff_value = calculate(10,5)
print(sum_val, diff_value)  
print(type(sum_val), type(diff_value)) 

sum_val = calculate(10,5)
print(sum_val, type(sum_val)) #tuple

# a , b = 9 , 12
# a , b = b , a #swaping of numbers
# print(a,b)




