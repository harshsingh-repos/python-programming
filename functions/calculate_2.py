
#program for quadratic equation

def quadratic(a,b,c,x): #paramters (a = 2 , b = 3, c = 4, x = 0.5) left-> right assignment
    first = a * x **2
    second = b * x
    third = c 
    return first + second + third

result = quadratic(2, 3, 4, 0.5)  #argument 
print(result)

result = quadratic(2, 3, 4, 1.5)  #argument 
print(result)