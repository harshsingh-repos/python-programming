
string = "H2R5HT2"
total = 0 # The sum of the digits in the string
count = 0 # the number of digits in the string

for index in range(len(string)):
    if string[index].isalpha():
        continue
    # print(string[index])
    total = total + int(string[index])
    count +=1

print(total)
print(count)

