
s = "aB:cD"
s = "JaCkSooNL:ALDIQQxoO"

# misunderstood just earlier


def transform_string(s):
    def transformer(st):
        ind = 0
        if st[ind].isupper():
            st.replace(st[ind], st[ind].lower())
        else:
            st.replace(st[ind], st[ind].upper())
        ind += 1
        return st
    colon = s.find(":")
    before_s = s[:colon]
    after_s = s[colon+1:]
    res = "{}:{}".format(transformer(before_s), transformer(after_s))
    return res

#now, misunderstood


def transform_string(s):
    colon = s.find(":")
    bef_s = "".join([x.upper() if x.islower() else x.lower()
                    for x in s[:colon]])
    aft_s = "".join([x.upper() if x.islower() else x.lower()
                    for x in s[colon+1:]])
    res = "{}:{}".format(bef_s, aft_s)
    return res


def transform_string():
    colon = s.find(":")
    first = s[:colon]
    last = s[colon+1:]
    res = "{}:{}".format(first.lower(), last.upper())
    return res


def transform_string():
    colon = s.find(":")
    first = s[:colon].lower()
    last = s[colon+1:].upper()
    res = "{}:{}".format(first, last)
    return res


# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below
print(transform_string(s))
print()  # extra newline at the end
