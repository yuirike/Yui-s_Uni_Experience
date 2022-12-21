#2022
#Implement a function length which takes a single parameter iterable, 
#which can be a list, tuple or string. 
# The function should compute the length of iterable recursively.
def length(iterable):
    if iterable == "" or iterable == [] or iterable == ():
        return 0 #end condition
    return 1 + length(iterable[1:])
    #if iterable[0] is not end condiiton, then its 1 and you add the rest.
print( length(("a", 1, 2, None)) )



#2021
#Implement a recursive function count, which takes a list l that contains arbitrary Elements, including nested lists. 
# The function should count the number of elements in l while specially treating each nested list:
#Their solution
def count(l):
    res = 0
    for e in l:
        if isinstance(e, list):
            res += count(e)
        else:
            res += 1
    return res
print(count([1, "", [{}], [[True], 4]]))


#2021 - Midterm
#Implement a function recursive_format, which takes a list tree as the only parameter. 
# tree can contain strings but also nested lists, which in turn again can contain both strings 
# and more deeply nested lists. The function should return a single string constructed from tree
#Their solution
def recursive_format(tree):
    elem = []
    for node in tree:
        if isinstance(node, str):
            elem.append(node)
        else: elem.append(f"({recursive_format(node)})")
    return " ".join(elem)
print(recursive_format(["Hi", "there", ["Jack", "and", "Bobby"], "!"]))


#2020
#My way, corrected...
def recursive_join(delim, values):
    if len(values) == 0:
        return ""
    else:
        res =  f"{values[0]}{delim}{recursive_join(delim,values[1:])}"
        res = res[:-1]
        return res

def recursive_join_theirs(delim, values):
    if len(values) == 1:
        return values[0]
    return values[0] + delim + recursive_join(delim, values[1:])
   
print(recursive_join(" <0> ", ["a","b","c","d","e"]))
print(recursive_join_theirs(" <0> ", ["a","b","c","d","e"]))


#Mentioned in Class
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



#Duplicate each nth element of a list.
def duplicate(n, current, l):
    if l == []:
        return []
    if current == 1:
        return [l[0],l[0]] + duplicate(n, n, l[1:])
    return [l[0]] +  duplicate(n, current-1, l[1:])

print(duplicate(3, 3, [1,2,3,4,5,6,7,8,9]))

#Double every number if its even
def double_if_even(l):
    if l == []:
        return []
    if l[0] % 2 == 0:
        return [l[0]*2] + double_if_even(l[1:])
    return [l[0]] + double_if_even(l[1:])

print(double_if_even([1,2,3,4,5,6,7,8]))


#Takes dictionary, returns all the values of the dictionary
def recursive_dict_to_list(d):
    if d == {}:
        return []
    key = list(d.keys())[0]
    value = d[key]
    del d[key]
    return [value] + recursive_dict_to_list(d)
print(recursive_dict_to_list({1:"A", 2:"B", 3:"C"}))

#Reverse a list 
def reverse(l):
    if l == []:
        return []
    return reverse(l[1:]) + [l[0]]
print(reverse([1,2,3,4,5,6,7]))