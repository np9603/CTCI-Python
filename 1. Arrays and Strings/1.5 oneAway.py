"""


"""

def oneEditReplace(s1,s2):

    editflag = False

    for c1,c2 in zip(s1,s2):
        if c1 != c2:
            if editflag:
                return False
            editflag = True

    return True


def oneEditInsert(s1,s2):

    editflag = False
    p1,p2 = 0,0

    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] != s2[p2]:
            if editflag:
                return False
            editflag = True
            p2 += 1
        else:
            p1 += 1
            p2 += 1

    return True


def oneAway(s1,s2):

    print(s1,s2,end=" ")
    if len(s1) == len(s2):
        return oneEditReplace(s1,s2)
    elif len(s1) + 1 == len(s2):
        return oneEditInsert(s1,s2)
    elif len(s1) == len(s2) + 1:
        return oneEditInsert(s2,s1)
    return False

print(oneAway("pale", "pale"))
print(oneAway("pale", "ple"))
print(oneAway("ples", "pales"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))
print(oneAway("pas", "pale"))
print(oneAway("ale", "elas"))

def oneAway2(s1,s2):

    len_diff = abs(len(s1)-len(s2))

    if len_diff > 1:
        return False

    if len(s1) > len(s2):
        longer,shorter = s1, s2
    else:
        longer,shorter = s2,s1

    p1,p2 = 0,0
    editflag = False

    while p1 < len(longer) and p2 < len(shorter):
        if longer[p1] != shorter[p2]:
            if editflag:
                return False
            editflag = True

            if len(longer) == len(shorter):
                p2+=1
        else:
            p2+=1
        p1+=1

    return True

print()
print(oneAway2("pale", "pale"))
print(oneAway2("pale", "ple"))
print(oneAway2("ples", "pales"))
print(oneAway2("pale", "bale"))
print(oneAway2("pale", "bake"))
print(oneAway2("pas", "pale"))
print(oneAway2("ale", "elas"))



