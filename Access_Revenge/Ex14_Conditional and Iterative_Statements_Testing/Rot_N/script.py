#!/usr/bin/env python3

# You can freely adopt these values to try your solution
# with different values.
plain_text = "A+z"
shift_by = 1

# perform a ROTn encoding
def rot_n():
    _A_ = ord("A") #65
    _Z_ = ord("Z") #90
    _a_ = ord("a") #97
    _z_ = ord("z") #122
    output = []
    shift = shift_by
    if shift == 0:
        encoded = plain_text
        return encoded
    

    elif shift > 0:
        shift = shift%26
        for i in plain_text:
            if not i.isalpha():
                output.append(i)
                continue
            elif i.isupper() and _Z_ < shift+ord(i):
                diff = shift+ord(i) - (_Z_+1)
                add = chr(_A_+diff)
                output.append(add)
            elif i.isupper() and _Z_ >= shift+ord(i):
                add = chr(shift+ord(i))
                output.append(add)
            elif i.islower() and _z_ < shift+ord(i):
                diff = shift+ord(i) - (_z_+1)
                add = chr(_a_+diff)
                output.append(add)
            elif i.islower() and _z_ >= shift+ord(i):
                add = chr(shift+ord(i))
                output.append(add)
    elif shift < 0:
        shift = abs(shift)%26
        for i in plain_text:
            if not i.isalpha():
                output.append(i)
            elif i.isupper() and _A_ > ord(i)-shift:
                diff = _A_ - (ord(i)-shift+1)
                add = chr(_Z_ - diff)
                output.append(add)
            elif i.isupper() and _A_ <= ord(i)-shift:
                add = chr(ord(i)-shift)
                output.append(add)
            elif i.islower() and _a_ > ord(i)-shift:
                diff = _a_ - (ord(i)-shift+1)
                add = chr(_z_-diff)
                output.append(add)
            elif i.islower() and _a_ <= ord(i)-shift:
                add = chr(ord(i)-shift)
                output.append(add)             

    encoded = "".join(output)
    return encoded

print(rot_n())

