#!/usr/bin/env python3

# You can freely adopt these values to try your solution
# with different values.
plain_text = "abzAZ!"
shift_by = 27

# perform a ROTn encoding
def rot_n():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    out_list = []
    text_list = []
    global shift_by
    if shift_by > 26:
        shift_by = shift_by - 26
    elif shift_by < -26:
        shift_by = shift_by + 26


    for i in plain_text:
        text_list.append(i)

    for i in text_list:
        if i.isalpha():
            if i.isupper():
                tra = ord(i)+shift_by
                if tra > 90:
                    tra = tra-26
                    out_list.append(chr(tra))
                elif tra < 65:
                    tra = tra+26
                    out_list.append(chr(tra))
                else:
                    out_list.append(chr(tra))
            elif i.islower():
                tra = ord(i)+shift_by
                if tra > 122:
                    tra = tra-26
                    out_list.append(chr(tra))
                elif tra < 97:
                    tra = tra+26
                    out_list.append(chr(tra))
                else:
                    out_list.append(chr(tra))
        else:
            out_list.append(i)

    encoded = "".join(out_list)
    
    # You don't need to change the following line.
    # It simply returns the string created above.
    return encoded

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(rot_n())

