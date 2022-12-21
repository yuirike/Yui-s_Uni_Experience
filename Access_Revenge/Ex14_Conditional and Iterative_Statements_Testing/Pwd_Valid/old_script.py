#!/usr/bin/env python3

pwd = "abc**"

def is_valid():
    # You need to change the following part of the function
    # to determine if it is a valid password.
    pw = []
    xpw = []
    sp  = ["+", "-", "*", "/"]

    for i in pwd:
        pw.append(i)
    # print(pw)

    if len(pw) >= 8 and len(pw) <= 16:
        for i in pw:
            if i.isalpha():
                if i.isupper():
                    xpw.append(i)
                elif i.islower():
                    xpw.append(i)
            elif i.isdigit():
                xpw.append(i)
            elif i in sp:
                xpw.append(i) #xpw is indeed ["a","b","c"] after this one. Only the given signs get added.
    # print(xpw)
    # else:
    #     print("No")

    if len(xpw) == len(pw): #if xpw has the length as pw, then we can continue. otherwise, a sign would be missing.
        numL = sum(1 for c in pw if c.islower())
        numU = sum(1 for c in pw if c.isupper())
        numD = sum(1 for c in pw if c.isdigit())
        numC = xpw.count("+") + xpw.count("-") + xpw.count("*") + xpw.count("/")
        if numL >= 2 and numU >= 2 and numD >= 2 and numC >= 2:
            validity = True
        else:
            validity = False
    else:
        validity = False

    # You don't need to change the following line.
    return validity

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())

