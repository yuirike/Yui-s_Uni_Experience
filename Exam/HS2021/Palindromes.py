def count_palindromes(sentece):
    sentece = sentece.lower().split(" ")
    counts = 0
    for i in sentece:
        word = [x for x in i if x.isalpha()]
        word_rev = [x for x in reversed(word)]
        if word == word_rev and len(word)>=3:
            counts += 1
    return counts



assert count_palindromes("Having fun!") == 0
assert count_palindromes("Bob and otto") == 2
assert count_palindromes("Where's Dad?") == 1
assert count_palindromes("Otto is my dad.") == 2
assert count_palindromes("I don't like pop music") == 1