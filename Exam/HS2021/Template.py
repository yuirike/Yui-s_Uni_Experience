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
    
        
class Extra(Actor):
    def __init__(self, name, hourly_salary, hours_per_month):
        Actor.__init__(self, name)
        self.__hourly_salary = hourly_salary
        self.__hours_month = hours_per_month

        if hourly_salary < 9.4:
            raise ValueError

    def get_monthly_salary(self):
        return self.__hours_month*self.__hourly_salary

    def __str__(self):
        return f"Salary: {self.get_monthly_salary()} (temp)"


class Studio:
    def __init__(self, name):
        self.name = name
        self.__staff = []

    def add_actor(self, actor):
        if actor in self.__staff:
            raise ValueError

        self.__staff.append(actor)

    def get_monthly_staff_cost(self):
        output = []
        for i in self.__staff:
            output.append(i.get_monthly_salary())
        return sum(output)




#Assertions
e = Studio("Warmer Sisters")
i1 = Lead("Bob", 60000) # yearly salary
i2 = Lead("Alice", 75000) # yearly salary
i3 = Extra("Taylor", 21.50, 15) # hourly salary, hours per month
assert i1.get_name() == "Bob"
assert i3.get_name() == "Taylor"
assert i1.get_id() == 0
assert i2.get_id() == 1
assert i1.get_monthly_salary() > 4000
assert i3.get_monthly_salary() == 322.50
e.add_actor(i1)
e.add_actor(i2)
e.add_actor(i3)
assert e.get_monthly_staff_cost() > 9000