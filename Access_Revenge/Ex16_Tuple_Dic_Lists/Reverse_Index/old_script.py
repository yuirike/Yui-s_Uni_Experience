from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    if dataset == []:
        return {}
    def tester(x,y): #created to be able to run values from a list through the code; finds index values
        z=[]
        check = []
        for i in y: #for i in list a:
            if i in check:
                z.append(y.index(i)+check.count(i))
                check.append(i)
                continue
            if x in i: #if x (which is q, an element of b) is in i (string)
                z.append(y.index(i)) #append the index of i where x is inside of it.
                check.append(i)
        return z

    #x = word, like "hello"
    #y = list, lower case of data set
    #z = list containing the indices of word
    #note, data set has three strings but not three words
    #hello appears twice
    e = []
    a = [x.lower() for x in dataset]
    for i in a:
        op = i.split()
        e.append(op)
    # print(a)

    # z=[]
    # for i in a:
    #     if "hello" in i: #how to use this for multiple
    #         z.append(a.index(i))
    # print(z)

    l = " ".join(a)
    # print(l)
    b = l.split(" ")
    b = list(set(b)) #Set contains each word that should become a key and will be looked for in list.
    # b = sorted(b)
    # print(b)

    l1 = []
    for q in b:
        l1.append(tester(q,e))

    # print(list)
    # print(b)
    # print(a)
    dictionary = dict(zip(b,l1))
    return dictionary

    # don't forget to return your resulting dictionary

# You can see the output of your function here
print(reverse_index(dataset))
