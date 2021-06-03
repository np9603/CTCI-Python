"""


"""

def stringComp(s1):

    if len(s1) == 0:
        return s1

    ans = []
    index = 0
    counter = 1

    while index < len(s1) - 1:
        if s1[index] == s1[index+1]:
            counter+=1
        else:
            ans.append(s1[index] + str(counter))
            counter = 1

        index+=1

    ans.append(s1[index] + str(counter))
    ans = "".join(ans)
    return ans if len(ans) < len(s1) else s1

print(stringComp("aabcccccaaa"))
print(stringComp("abcdef"))
print(stringComp("aabb"))
print(stringComp("aaa"))
print(stringComp("a"))
print(stringComp(""))


