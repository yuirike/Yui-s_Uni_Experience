#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):
        return None
    else:
        f = open(path, "r")
        lines=f.readlines()
        avg = []
        null = []
        for line in lines:
            str(line)
            if str("#") in line:
                continue
            if len(line) == 0:
                avg.append(0.0)
            if ":" in line:
                colon_ind = line.index(":")+1
                after_colon = line[colon_ind:]
                make_float = float(after_colon)
                avg.append(make_float)
                avg_grade = sum(avg)/len(avg)

        if avg == []:
            return 0.0
        else:
            return avg_grade



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("public/my_grades.txt"))

