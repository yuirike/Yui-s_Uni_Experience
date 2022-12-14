from collections import defaultdict

dataset = [
    "Hello     world",
    "This is the    WORLD",
    "hello    again"
 ] 


def reverse_index(dataset):
    data = [x.lower().split(" ")for x in dataset]
    single = []
    for i in data: single.extend(i)   
    single = list(set(single))
    if '' in single: single.remove('')
    index_dictionary = {}

    for key_word in single:
        index_list = []
        for index_num,string_list in enumerate(data):
            if key_word in string_list: index_list.append(index_num)
            index_dictionary[key_word]=index_list
    return index_dictionary

    # don't forget to return your resulting dictionary

# You can see the output of your function here
print(reverse_index(dataset))
# for i in reverse_index(dataset).items():
#     print(i)
