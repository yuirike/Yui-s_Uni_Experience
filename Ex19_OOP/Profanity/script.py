#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = template
    


    def filter(self, msg):
        censor = []
        c_len = len(self.__template)
        pass

            



# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno


#Figuring out repeated loops.
tp = "kek"
top = "MyBad"
p =[]
tp = [x for x in tp]

for i in top:
    p.append(tp[0])
    tp.append(tp[0])
    tp.pop(0)

print(p)



