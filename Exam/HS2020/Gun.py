import random

class Revolver:
    def __init__(self, cylinder_size):
        self.__cylinder_size = cylinder_size
        self.__chamber = [0 for x in range(cylinder_size)]
        self.reload()

    def reload(self):
        if len(self.__chamber) != self.__cylinder_size:
            self.__chamber = [0 for x in range(self.__cylinder_size)]

        if not 1 in self.__chamber:
            self.__chamber.remove(0)
            self.__chamber.append(1)
        
    def trigger(self):
        if self.__chamber == []:
            self.__chamber.append(0)

        shot = random.choice(self.__chamber)
        if shot == 0:
            self.__chamber.remove(0)
            return "Click!"
        if shot == 1:
            self.__chamber.remove(1)
            return "BANG!!!"

    def get_stuff(self):
        return self.__chamber

R = Revolver(6)
print(R.get_stuff())
gun = Revolver(6)
turns = [gun.trigger() for i in range(10)]
assert("BANG!!!" in turns[0:6])
assert("BANG!!!" not in turns[6:])

gun.reload()
turns = [gun.trigger() for i in range(10)]
assert("BANG!!!" in turns[0:6])
assert("BANG!!!" not in turns[6:])