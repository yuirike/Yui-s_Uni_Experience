pwd = "aaAA00++#"
def is_valid():
    if not len(pwd) in [x for x in range(8, 17)]:
        return False
    low_let = []
    up_let = []
    digit = []
    spec = []
    char_check = True
    everything = "{}{}{}{}".format("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", "".join(["+", "-", "*", "/"]))
    for i in pwd:    
        if i.islower(): low_let.append(i)
        if i.isupper(): up_let.append(i)
        if i.isdigit(): digit.append(i)
        if i in ["+", "-", "*", "/"]: spec.append(i)
    for i in pwd:
        if not i in everything: char_check = False

    if len(low_let) >= 2 and len(up_let) >= 2 and len(digit) >= 2 and len(spec) >= 2 and char_check is True: validity = True
    else: validity = False
    return validity
print(is_valid())


