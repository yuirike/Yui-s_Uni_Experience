def char_multiplier(s, l):
    copy = l.copy()
    new_l = []
    for char in s:
        new_l.append(copy[0])
        copy.append(copy[0])
        copy.pop(0)
    return new_l


def intersperse(s,l):
    s = [x for x in s]
    new_s = []
    l = char_multiplier(s, l)
    for a, b in zip(s,l):
        new_s.append(a)
        new_s.append(b)
    new_s.pop()
    new_s = "".join(new_s)
    return new_s


assert intersperse("H", [',']) == "H"
assert intersperse("Hello", [',']) == "H,e,l,l,o"
assert intersperse("Hello", [',', '.']) == "H,e.l,l.o"
assert intersperse("Hello", ['', '.']) == "He.ll.o"
assert intersperse("Hello", ['-o-', '_o_']) == "H-o-e_o_l-o-l_o_o"
assert intersperse("Hello", [',', '.', '-']) == "H,e.l-l,o"


