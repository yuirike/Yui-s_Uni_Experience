class Event:
    def __init__(self, name, seats):
        self.__name = name
        self.__seats = [x for x in range(seats+1) if x != 0]
        self.__available = {x: 0 for x in self.__seats}

    def enter(self, seat, name):
        if seat < 1 or seat > len(self.__seats):
            raise IndexError
        if self.__available[seat] != 0:
            raise NameError
        occ = {seat: name}
        self.__available.update(occ)

    def get(self, seat):
        if seat < 1 or seat > len(self.__seats):
            raise IndexError
        if self.__available[seat] == 0:
            return None
        return self.__available[seat]

    def occupied(self):
        val = [x for x in self.__available.values()]
        val = [x for x in val if x != 0]
        return len(val)

    def empty(self):
        val = [x for x in self.__available.values()]
        val = [x for x in val if x == 0]
        return len(val)

    def __eq__(self, other):
        return self.occupied() == other.occupied()

    def __gt__(self, other):
        return self.occupied() > other.occupied()

    def __lt__(self, other):
        return self.occupied() < other.occupied()


P = Event("Name", 10)
P.enter(5, "Jason")
print(P.occupied())
print(P.empty())
print(P.get(5))


A = Event("Kek", 10)
A.enter(5, "Bea")
print(A.occupied())
print(A.empty())
print(A.get(5))

print(A == P)
