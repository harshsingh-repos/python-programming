#Display one charater per line

'''
data = input("Enter a line of text: ")

if len(data) > 0:
    for letter in data:
        print(letter)
else:
    print("User input missing")

# count = 0 
# while count < len(data):
#     letter = data[count]
#     print(letter)
#     count +=1 
'''
# Count the charater in a string

data = input( "Enter a String: ")

count = 0
# for ch in data:
#     if ch == 'a':
#         count +=1

# print(f"The count of charater 'a' is : {count} times")

for ch in data:
    if ch in ('a', 'A'):
        count +=1

print(f"The count of charater 'a' is : {count} times")