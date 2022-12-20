def is_isogram(sentence):
    if type(sentence) != str:
        raise TypeError
    if sentence == "":
        raise ValueError
    check = "".join(x for x in sentence if x.isalpha())
    if len(check) == 0:
        raise TypeError
    
    sentence = [x for x in sentence.lower() if x.isalpha()]
    char_check = sentence.copy()
    sentence = "".join(sentence)
    counts = []
    for char in char_check:
        counts.append(sentence.count(char))
    if len(counts)*counts[0] == sum(counts):
        res = True
    else:
        res = False
    return res


assert is_isogram("uncopyrightable")
assert is_isogram("The big dwarf only jumps.")
assert (not is_isogram("bass"))
assert (not is_isogram("Tart"))
assert is_isogram("Apple-ale")
