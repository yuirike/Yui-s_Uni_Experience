def words_by_len(sentence):
    if type(sentence) != str:
        raise AssertionError   
    sentence = sentence.split(" ")

    lengths = [x for x in sentence if x !=""]
    lengths = list(set([len(x) for x in lengths]))
    words = []

    for length in lengths:
        same = []
        for word in sentence:
            if len(word) == length:
                same.append(word)
        words.append(same)

    res = {}
    lengths = sorted(lengths)
    words = [set(x) for x in words]
    words = sorted(words)
    for length, word in zip(lengths, words):
        res[length]=set(word)
    
    return res


assert words_by_len("how are ya?") == {3: {"how", "are", "ya?"}}
assert words_by_len(" I'm      so so ") == {2: {"so"}, 3: {"I'm"}}
assert words_by_len("Get well soon !!") == {2: {"!!"}, 3: {"Get"}, 4: {"well", "soon"}}
assert words_by_len("") == {}