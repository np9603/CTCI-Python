"""Given two strings, write a method to decide if one is a permutation of the other"""

str1 = "abcde"
str2 = "acbde"
str3 = "abcd"

def checkPermutation(str1,str2):

    str1 = sorted(str1)
    str2 = sorted(str2)
    # print(str1,str2)
    return str1==str2

print(checkPermutation(str1,str2))
print(checkPermutation(str1,str3))

def checkPermutation2(str1,str2):

    if len(str1) != len(str2):
        return False

    charmap = [0] * 256

    for char in str1:
        charmap[ord(char)] += 1

    for char in str2:
        charmap[ord(char)] -= 1

    for index in range(256):
        if charmap[index]:
            return False

    return True

print(checkPermutation2(str1,str2))
print(checkPermutation2(str1,str3))