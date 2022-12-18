#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_average_grade(path):
    if not os.path.exists(path):
        return None

    with open(path) as file:
        data = file.readlines()
    if data == []:
        return 0.0

    data = [x.strip() for x in data]
    data = [x.replace(x[x.find('#'):], "") if '#' in x else x for x in data]
    data = [x[x.find(':')+1:] if ':' in x else x for x in data]
    data = [x.strip() for x in data]
    data = [float(x) for x in data if is_number(x)]
    avg = sum(data)/len(data)
    return avg


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
# print(get_average_grade("public/my_grades.txt"))

print(get_average_grade("my_grades.txt"))
