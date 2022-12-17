def compress(data):
    def dic_to_output(dic, outer_list):
        items = []
        for i in dic.items():
            items.append(i)
        items.sort()
        # print(items)
        key_list = []
        value_list = []
        # outer_list = []
        inner_list = []

        for i in items:
            key_list.append(i[0])
            value_list.append(i[1])
        outer_list.append(tuple(key_list))
        inner_list.append(tuple(value_list))
        outer_list.append(inner_list)
        outer_tuple = tuple(outer_list)
        return outer_tuple

    a = []
    b = ()
    c = ()
    l = c + (b, a)
    if data == []:
        return l
    x = ()
    y = ()
    p = [()]
    new = x+(y, p)
    if data == [{}]:
        return new
    lis = []
    for i in data:
        output = dic_to_output(i, lis)
    output = list(output)
    clear = []
    for i in data[0]:
        clear.append(i)
        clear.sort()

    clear = tuple(clear)
    for i in output:
        if clear in output:
            output.remove(clear)
    old_tuple = output
    new_out = []
    for i in old_tuple:
        new_out = new_out+i
    l = []
    l.append(new_out)
    l.insert(0, clear)
    return tuple(l)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]
print(compress(data))
