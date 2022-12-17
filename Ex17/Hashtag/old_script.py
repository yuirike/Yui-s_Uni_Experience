#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def breaker(string_value):
    s = ''.join(filter(str.isalnum, string_value))
    return s

def analyze(posts):
    comma_join = ",".join(posts)
    space_join = comma_join.replace(",", " ")
    item_list = space_join.split(" ")
    hash_list = []
    for i in item_list:
        if "#" in i:
            if len(i) > 1 and i[1].isdigit():
                continue
            if i == "#":
                continue
            hash_list.append(i)
    data = {}
    for i in hash_list:
        j = item_list.count(i)
        i = i.replace("#","")
        if not i.isalnum():
            i = breaker(i)
        data.update({i:j})
    return data


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = ['#1abc']
print(analyze(posts))
