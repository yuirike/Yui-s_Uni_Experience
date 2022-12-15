from their_script import analyze2


def split_at(x):
    for i in x[1:]:
        if not i.isalnum():
            return x[:x.index(i)]


def analyze(posts):
    # turn the string into a nested list.
    str_to_list = [x.split() for x in posts]
    word_list = []
    for i in str_to_list:
        word_list.extend(i)
    only_hash = [x for x in word_list if '#' in x]
    only_hash = [x[x.find('#'):] for x in only_hash]
    only_hash = [x if x[1:].isalnum() else split_at(x) for x in only_hash]
    keys = list(set([x[1:] for x in only_hash if x[1].isalpha]))
    keys_with = list(set(x for x in only_hash if x[1].isalpha))
    keys.sort()
    keys_with.sort()
    output = {}
    for a, b in zip(keys, keys_with):
        output[a] = only_hash.count(b)

    return output


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morhjloh.lon.lb.libningb.lonoön#zurich #limmat",
    "spend my #weekend in #zur.on.öonloich",
    "#zur,ich <3"]
print(analyze(posts))


# Their script, for comparison.
print(analyze2(posts))
print(analyze(posts) == analyze2(posts))
