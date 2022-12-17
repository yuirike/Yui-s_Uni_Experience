#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class ProfanityFilter:
    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = template

    def filter(self, msg):
        censor_dictionary = {}
        censor = [x for x in self.__template]
        censored_words = []
        # key_w = self.__keywords.copy()

        for word in self.__keywords:
            censored_word = []  # for each word in keywords, create a list.
            copy = censor.copy()  # make a copy of the censor
            for letter in word:
                # append for each letter in word, the first letter of copy (censor)
                censored_word.append(copy[0])
                copy.append(copy[0])  # append that letter to the end of copy
                copy.pop(0)  # remove first letter of copy
            # add that joined list to censored_words.
            censored_words.append("".join(censored_word))

        censored_words = list(set(censored_words))

        new_msg = msg.lower()
        for i in self.__keywords:
            if i in new_msg:
                temp = [x for x in censored_words if len(x)==len(i)]
                new_msg = new_msg.replace(i, temp[0])


        output = []
        for a, b in zip(msg, new_msg):
            if a.lower() == b:
                output.append(a)
            else:
                output.append(b)

        output = "".join(output)
        return output


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["mastard", "duck", "shot", "batch"], "?#$")
    offensive_msg = "mastard duck shot test?"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno

