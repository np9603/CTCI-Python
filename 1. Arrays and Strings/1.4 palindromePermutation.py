"""


"""

str1 = "Tact Coa"

def palindromePerm(string):

    string = string.lower()
    charset = set()

    for char in string:
        if char.isalnum():
            if char not in charset:
                charset.add(char)
            else:
                charset.remove(char)
    print(charset)
    return len(charset) == 1



print(palindromePerm(str1))

