#program to check palindrome 
import math
def checkPalindrome(text):
    index  = len(text)
    half = index // 2
    for i in range(half):
        if(text[i]==text[index-1-i]):
            half -=1
            if half == 0:
                return "plaindrome"
        else:
            return "Not plaindrome"

# checkPalindrome("madam")

print(checkPalindrome("madam"))  # ✅ True
print(checkPalindrome("hello"))  # ❌ False
print(checkPalindrome("racecar"))  # ✅ True
print(checkPalindrome("Python"))  # ❌ False
print(checkPalindrome("hello"))  # ❌ False
