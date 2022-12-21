#!/usr/bin/env python3

plain_text = "A+z"
shift_by = 1

# perform a ROTn encoding
def rot_n():
    # "normalize" shift by to the smallest positive shift
    shift_by_normal = shift_by % 26

    # lets define some helper variables
    ordA = ord("A") # 65
    ordZ = ord("Z") # 90
    orda = ord("a") # 97
    ordz = ord("z") # 122

    encoded = ""
    for c in plain_text:

        # just append all non-letters
        if not c.isalpha():
            encoded += c
            continue

        # calculate new ascii code
        o1 = ord(c)
        o2 = o1 + shift_by_normal

        # handle "overflow" (ascii code points beyond z/Z)
        if o1 <= ordZ and o2 > ordZ:
            delta = o2 - ordZ - 1 # -1 to compensate for "A" being included
            o2 = ordA + delta

        elif o1 <= ordz and o2 > ordz:
            delta = o2 - ordz - 1 # -1 to compensate for "a" being included
            o2 = orda + delta

        encoded += chr(o2)

    print("ROT{}({}) = {}".format(shift_by, plain_text, encoded))
    return encoded

print(rot_n())