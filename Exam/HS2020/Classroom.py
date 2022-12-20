class Classroom:
    def __init__(self):
        self.students = {}

    def add(self, s):
        if s.matno in self.students.keys():
            raise ValueError

        self.students[s.matno]=s

    def remove(self, s):
        if not s in self.students.keys():
            raise IndexError
        self.students.pop(s)
      

class Student:
    ID = -1
    def __init__(self, fname, lname):
        Student.ID += 1
        self._fname = fname
        self._lname = lname
        self.matno = Student.ID





s1 = Student("Alice", "Bauer")
s2 = Student("Jack", "Wonderland")
assert(s1.matno == 0)
assert(s2.matno == 1)
c = Classroom()
c.add(s1)
c.add(s2)
assert(len(c.students) == 2)
c.remove(s2.matno)
assert(len(c.students) == 1)
try: # adding a student already in c
    c.add(s1)
    assert(False) # expected a ValueError!
except ValueError:
    pass # the correct exception has been thrown
try: # removing a student not in c
    c.remove(s2.matno)
    assert(False) # expected a ValueError!
except IndexError:
    pass # the correct exception has been thrown