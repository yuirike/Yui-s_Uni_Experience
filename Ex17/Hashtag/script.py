def split_at(x):
    for i in x[1:]:
        if not i.isalnum():return x[:x.index(i)]

def analyze(posts):
    str_to_list = [x.split() for x in posts] #turn the string into a nested list. 
    word_list = []
    for i in str_to_list: word_list.extend(i) #get a list of words
    keys = list([x for x in word_list if x[0]=='#' and x[1].isalpha()]) #make a list of keys
    keys_without = list([x.replace('#','') for x in word_list if x[0]=='#' and x[1].isalpha()]) #make a list of keys without '#'
    keys_without = [split_at(x) if not x.isalnum() else x for x in keys_without] #create appropriate keys
    keys = [split_at(x) if not x[1:].isalnum() else x for x in keys]
    keys = list(set(keys))
    keys_without = list(set(keys_without))
    keys.sort()
    keys_without.sort()
    #sort lists to let zip() do the magic.
  
    output = {}
    for key,key_w in zip(keys, keys_without):
        output[key_w]=str(word_list).count(key)

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



from their_script import analyze2
print(analyze2(posts))
print(analyze(posts) == analyze2(posts))

