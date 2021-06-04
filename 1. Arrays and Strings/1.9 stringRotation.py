"""


"""

s1 = "waterbottle"
s2 = "erbottlewat"
s3 = "bottlewat"

def stringRotation(s1,s2):

    if len(s1) != len(s2):
        return False

    if len(s1) == 0:
        return True

    s = s1 + s1

    return s2 in s

print(stringRotation(s1,s2))
print(stringRotation(s1,s3))