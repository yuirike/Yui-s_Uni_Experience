#!/usr/bin/env python3

s = "ljddöLLLL:KKéLKökö"

# perform the transformation
def transform_string():
    # Insert your code here.
    # You may want to use several variables to
    # store temporary values (such as the index of
    # the colon or the two strings before and after
    # it). Then, you can construct the final result
    # from your temporary variables.
    found = s.find(':')
    first = s[:found]
    found = found+1
    last = s[found:]
    res = f'{first.lower()}:{last.upper()}'

    # You don't need to change the following line.
    # It simply returns the string created above.
    return res

# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below
print(transform_string())
print() # extra newline at the end
