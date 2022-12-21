def encode(word, add, shift):
    word = [x for x in word]
    add = [x for x in add]
    copy = add.copy()
    new_add = []
    for letter in word:
        new_add.append(copy[0])
        copy.append(copy[0]) 
        copy.pop(0)  
    new_word = []
    for a, b in zip(word, new_add):
        new_word.append(a)
        new_word.append(b)
    
    assci_list = [ord(x)+shift for x in new_word]
    asscii_word = [chr(x) for x in assci_list]
    asscii_word = "".join(asscii_word)
    return new_word, assci_list, asscii_word

def decode(word, add, shift):
    bef_ord_word = [ord(x) for x in word]
    ord_word = [ord(x)+2 for x in word]
    word = [chr(x) for x in ord_word]

    changed = [x for x in word if not x in add]
    changed_word = "".join(changed) #I'm aware that this doesn't work...
    return bef_ord_word, word, changed_word

print(encode("hello", "xyz", -2))
