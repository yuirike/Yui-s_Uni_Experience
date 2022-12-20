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



#Assertions
e1 = Event("Name", 150)
e1.enter(45, "Alice")
assert e1.get(45) == "Alice"
e1.enter(42, "Bob")
assert e1.occupied() == 2
assert e1.empty() == 148
e2 = Event("Nalo", 40)
assert e2.get(40) == None
e2.enter(1, "Andrea")
e2.enter(2, "Beatrice")
assert e2 == e1
e2.enter(20, "Charly")
assert e2 > e1