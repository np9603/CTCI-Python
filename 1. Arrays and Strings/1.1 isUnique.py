"""Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?"""

str1 = "abcde"
str2 = "abcdeee"

def isUnique(str):
    seen = set()

    for char in str:
        if char in seen:
            return False
        else:
            seen.add(char)

    return True

print(isUnique(str1))
print(isUnique(str2))

def isUnique2(str):

    for i in range(0,len(str)-1):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return False

    return True

print(isUnique2(str1))
print(isUnique2(str2))


