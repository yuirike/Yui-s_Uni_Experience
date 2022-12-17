#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    if data == []:
        return ((),[])

    if len(data) > 0:
        verify = [x for x in data if x == {}]
    if len(verify) == len(data):
        return ((),[()])
    
    data = [x for x in data if x != {}]
    keys = [x for x in data[0].keys()]
    keys = sorted(keys)
    res  = []

    for dic in data:
        val = []
        for key in keys:
            val.append(dic[key])
        res.append(val)

    res = [tuple(x) for x in res]
    output = tuple([tuple(keys), res])
    return output


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [{}]
print(compress(data))

data2 = []
print(compress(data2))

data3 = [{"a":3, "b":4, "c":9}, {"a":"H", "b":"I", "c":"V"}, {}]
print(compress(data3))
