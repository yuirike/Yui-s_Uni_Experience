#2022
def length(iterable):
    if iterable == "" or iterable == [] or iterable == ():
        return 0 #end condition
    return 1 + length(iterable[1:])
    #if iterable[0] is not end condiiton, then its 1 and you add the rest.


#2021
#not fully correct
def count(l):
    l = [x for x in l if x != []]
    if l == []:
        return 0
    return 1 + count(l[1:])
# print(count([[],[],1]))

#Their solution
def count(l):
    res = 0
    for e in l:
        if isinstance(e, list):
            res += count(e)
        else:
            res += 1
    return res


#Their solution
def recursive_format(tree):
    elem = []
    for node in tree:
        if isinstance(node, str):
            elem.append(node)
        else: elem.append(f"({recursive_format(node)})")
    return " ".join(elem)
# print(recursive_format(["Hi", "there", ["Jack", "and", "Bobby"], "!"]))


#Was almost correct...
def recursive_join(delim, values):
    if len(values) == 1:
        return values[0]
    return f"{values[0]}{delim}{recursive_join(delim,values[1:])}"
   
print(recursive_join(" ", ["Hello", "world"]))

#My way, corrected...
def recursive_join(delim, values):
    if len(values) == 0:
        return ""
    else:
        res =  f"{values[0]}{delim}{recursive_join(delim,values[1:])}"
        res = res[:-1]
        return res
   
print(recursive_join(" <0> ", ["a","b","c","d","e"]))



p = "main Text main"
print(p[0:p.rfind("main")])



#Sum of a list of numbers.
def recsum(l):
    if l == []:
        return 0
    return l[0]+recsum(l[1:])

print(recsum([1,2,3,5]))

#Function, which adds one number to each number of a list:
def addsomething(n, l):
    if l == []: return []
    elem = l[0]+n
    return [elem] + addsomething(n,l[1:])

print(addsomething(4,[1,2,1,2]))

