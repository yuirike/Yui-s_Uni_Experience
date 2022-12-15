from their_script import analyze2

posts = ["hi #weekend",
         "good morning #zurich #limmat",
         "spend my #weekend in #zurich",
         "#edge,case", "###fuck###you###", '12kjl,ioj#HOJO', '1###', '#p']


# takes care of words such as "####aadk###snkdnls###"
def take_hash(x):
    if x.count('#') > 1:
        out = []
        for i in x.split('#'):
            if i.isalpha():
                out.append(f'#{i}')
        if x[0].isalpha() and x[0] in out[0]:
            out.remove(out[0])
        return out

    elif x.count('#') == 1:
        return x[x.find('#'):]


# splits words at non-aplhanumeric characters
def split_at(x):
    if not x[1:].isalnum():
        for i in x[1:]:
            if not i.isalnum():
                return x[:x.find(i)]
    return x


# bad implementation in hindsight, their solution did it with nested loops
# i guess it's a good lesson about list comprehension?
def analyze(posts):
    if posts == []:
        return {}  # empty list
    if str(posts).count('#') < 1:
        return {}  # hashtag count in general

    words = [x.split(' ') for x in posts]
    hash_words = []
    for x in words:
        hash_words.extend(x)  # all words

    # apply the filter to remove ugly ones.
    hash_words = list(map(take_hash, hash_words))
    hash_new = []
    for i in hash_words:
        if type(i) == str:
            hash_new.append(i)
        elif type(i) == list:
            # output is list, renew hashwords. could have been done in the function...
            hash_new.extend(i)

    # only take the ones that start with #
    hash_words = [x for x in hash_new if x[0] == '#']
    # hash_words = list(map(take_hash, hash_words))
    hash_words = list(map(split_at, hash_words))
    # remove hashtags which end with it or are only it.
    hash_words = [x for x in hash_words if x[-1] != '#']
    # only look at those with hashtag at start and alpha at second.
    hash_words = [x for x in hash_words if x[0] == '#' and x[1].isalpha()]
    keys = list(set([x[1:] for x in hash_words]))
    keys_w = list(set(hash_words))
    keys.sort()
    keys_w.sort()
    # you turn them into keys with and without hashtags.
    # remove the dupes and turn them into lists
    # sort them as you can now loop through them in zip()
    # check if the key_with is in hash_words and assign "key"
    # as the key of the dictionary.

    output = {}
    for key, key_w in zip(keys, keys_w):
        output[key] = hash_words.count(key_w)
    return output


print(analyze(posts))
print(analyze2(posts))
print(analyze(posts) == analyze2(posts))
