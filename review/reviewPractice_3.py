# To find the spaces in the sentences entered by the user

#1. user inputs a sentence
#2. Iterate over the characters in the sentence
#3. count the spaces " "
#4. return the count of spaces in a sentence
sentence = input("Enter a sentence: ")
'''
spaces =0
for character in sentence:
    if character == " ":
        spaces +=1
print("your string had ", spaces , "Spaces in it.")
'''
'''
spaces = 0
counter  =0 
while counter < len(sentence):
    if sentence[counter] == " ":
        spaces +=1
    counter +=1

print("your string had ", spaces , "Spaces in it.")
'''

print("Character at 0 index, 1 character: ", sentence[0])
print("Character at 1 index, 2 character: ", sentence[1])
print("Character at 2 index, 3 character: ", sentence[2])
print("Character at 3 index, 4 character: ", sentence[3])
print("Character at 4 index, 5 character: ", sentence[4])