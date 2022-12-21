'''
Idea:
Generate a list with all Greg and one with all IFC tuples.
Then turn that into a dictionary
'''


def gregorian_to_ifc(day, month, leap=False):
    IFC = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    IFC_all = []
    for a in IFC:
        for b in range(29):
            IFC_all.append((b, a))

    IFC_all = [x for x in IFC_all if x[0] != 0]  # filtering 0 days
    IFC_all.append("Year Day")

    Greg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    Greg_all = []
    for a in Greg:
        for b in range(32):
            Greg_all.append((b, a))

    Greg_all = [x for x in Greg_all if x[0] != 0]  # filtering zero days
    removal = [(29, 2), (30, 2), (31, 2), (31, 4), (31, 6), (31, 9), (31, 11)]
    # filtering non-existing tuples
    Greg_all = [x for x in Greg_all if x not in removal]

    IFC_all.pop()
    IFC_all.append("Year Day")

    if leap == True:
        # add the 29th and shift the whole thing.
        Greg_all.insert(Greg_all.index((28, 2))+1, (29, 2))
        Greg_all.append("Year Day")
        if (day, month) not in Greg_all:
            raise Warning("Invalid Input")

    dictionary = {}
    for a, b in zip(Greg_all, IFC_all):
        dictionary[a] = b

    if (day, month) not in Greg_all:
        raise Warning("Invalid Input")

    return dictionary[(day, month)]
