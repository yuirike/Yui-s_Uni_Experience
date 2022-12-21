class ProfanityFilter:

    def __init__(self, keywords, template):
        '''
        Probably, the only OOP part.
        '''
        self.__keywords = keywords
        self.__template = template

    def case_permutator(want):
        '''
        Stolen function, creates permutations of all lower/upper cases.
        I'm a bad person, I know. I modified it as well.
        '''
        def all_casings(input_string):
            if not input_string:
                yield ""
            else:
                first = input_string[:1]
                if first.lower() == first.upper():
                    for sub_casing in all_casings(input_string[1:]):
                        yield first + sub_casing
                else:
                    for sub_casing in all_casings(input_string[1:]):
                        yield first.lower() + sub_casing
                        yield first.upper() + sub_casing

        desired = [x for x in all_casings(want)]
        return desired

    def censor_maker(temp, rep):
        '''
        Uses template and length of the curse () to create a list of
        censor characters.
        '''
        list_in = []
        for i in temp:
            list_in.append(i)
        list_copy = list_in.copy()
        list_out = []
        r = 0
        while r != rep:
            list_out.append(list_copy[0])
            list_copy.pop(0)
            if list_copy == []:
                list_copy = list_in.copy()
            r = r+1
        return list_out

    def replacer(curse, list):
        '''
        Replaces each character of the curse.
        '''
        curse = "".join(list)
        return curse

    def filter(self, msg):
        new_key = []
        for i in self.__keywords:
            new_key.append(ProfanityFilter.case_permutator(i))

        '''
        Stolen line
        '''
        flat_list = [item for sublist in new_key for item in sublist]
        flat = sorted(flat_list, key=len)
        flat.reverse()
        for i in flat:

            if i in msg:
                censor = ProfanityFilter.censor_maker(self.__template, len(i))

                new = ProfanityFilter.replacer(i, censor)
                msg = msg.replace(i, new)

        return msg
