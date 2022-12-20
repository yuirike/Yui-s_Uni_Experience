import random

class Student:
    def __init__(self, name):
        self.__name = name
        self.__year = 1

    def learn(self):
        self.__year += 1  

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year


class School:
    national_taught = 0
    def __init__(self, name, years):
        self.__name = name
        self.__years = years
        self.__success = 0

    def educate(self, Student):
        if not Student.get_year() in self.__years:
            raise ValueError

        chance = [1,1,1,1,1,1,1,1,1,0]
        success = random.choice(chance)
        if success == 1:

            Student.learn()
            self.__success += 1
            School.national_taught +=1
    
    def get_taught(self):
        return self.__success



a = Student("Ueli")
assert a.get_name() == "Ueli"
assert a.get_year() == 1
s1 = School("Mätteliwise", [1,2,3,4,5,6])
s2 = School("Blüemlihof", [1,2,3,4,5,6])
assert s1.get_taught() == 0
# the following calls have random outcomes
s1.educate(a)
assert a.get_year() in [1, 2]
assert s1.get_taught() in [0, 1]
s2.educate(a)
assert a.get_year() in [1, 2, 3]
assert s2.get_taught() in [0, 1]
assert s2.national_taught in [0, 1, 2]

