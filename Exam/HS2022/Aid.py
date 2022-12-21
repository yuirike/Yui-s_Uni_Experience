def generic_func(variable):
    if variable == "Fuck":
        raise Warning
    return variable

def is_num(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#Dictionary Short-cut
raw = [('Math', 5.5), ('Biology', 5.75), ('Latin', 4.25), ('Latin', 3.5), 
                ('Biology', 4.5), ('Latin', 4.5), ('Biology', 4.75), ('French', 3.0)]

def avg_grade_per_subject(subjects_grades):
    avg_grade_per_subject = {}
    for subject, grade in subjects_grades:
        avg_grade_per_subject.setdefault(subject, []).append(grade)


    return avg_grade_per_subject
# print(avg_grade_per_subject(raw))

#Random
import random
# print(random.randint(0,9)) #Random integer between 0 and 9, probab 90% not 0.
# list = [1,1,1,1,0]
# print(random.choice(list)) #Picks an element out of a list, probab 80% not 0


#OOP - Inheritance
from abc import ABC, abstractmethod
class Actor(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def get_monthly_salary():
        pass

class Lead(Actor):
    ID = -1
    def __init__(self, name, annual_salary):
        Actor.__init__(self, name)
        Lead.ID += 1
        self.__ID = Lead.ID
        self.__annual_salary = annual_salary

    def get_id(self):
        return self.__ID

    def get_monthly_salary(self):
        return self.__annual_salary/12

    def __str__(self):
        return f"Salary: {self.get_monthly_salary()} ({self.__ID})"


#File handling
with open('test.txt') as file:
    data = file.readlines()
print(data)

with open('test.txt') as file:
    data = file.readlines()
print(data)

f = open("test.txt")
data = f.readlines()
f.close()
print(data)

# with open('test.txt', 'w') as file:
#     for i in data:
#         file.write(i)


#Function Tricks, Lambda
def func1(var):
    return lambda x: var+x
print(func1(5)(2))





#Maybe Useful Functions:
def flatten(l):
    return [item for sublist in l for item in sublist]







import unittest
class MyTestSuite(unittest.TestCase):
    def test_type_check(self):
        with self.assertRaises(Warning):
            generic_func("Fuck")

    def test_generc(self):
        a = "Kek"
        b = generic_func("Kek")
        self.assertEqual(a,b)