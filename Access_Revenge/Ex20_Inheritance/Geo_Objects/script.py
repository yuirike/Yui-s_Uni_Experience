'''
from cone import Cone
from cube import Cube

# Create first cone object
cone_1 = Cone(2, 4, 2, "red", True)
# Create another cone object
cone_2 = Cone(5.64, 4.2, 8.7, "black", False)
# Create a cube object
cube = Cube(7.2, "white", True)

print(f"Color of the cube object is: {cube.get_color()}")
# Update cube color
cube.set_color("yellow")
# See if the color of cube object is changed
print(f"Color of the cube object is: {cube.get_color()}")

# See the area and volume of the cone_1
print(
    f"cone_1 area is: {cone_1.get_area()} cone_2 volume is: {cone_1.get_volume()}")
'''

class Hey:
    def __init__(self, test):
        self.test = test
        self.PI = 3.14

class Hi(Hey):
    def __init__(self, test):
    
        self.__test = test

    def get_this(self):
        P = "{}+{}".format(self.__test, self.PI)
        return P

from cone import Cone
from cube import Cube

# Create first cone object
cone_1 = Cone(2, 4, 2, "red", True)
# Create another cone object
cone_2 = Cone(5.64, 4.2, 8.7, "black", False)
# Create a cube object
cube = Cube(7.2, "white", True)

print(f"Color of the cube object is: {cube.get_color()}")
# Update cube color
cube.set_color("yellow")
# See if the color of cube object is changed
print(f"Color of the cube object is: {cube.get_color()}")

# See the area and volume of the cone_1
print(
    f"cone_1 area is: {cone_1.get_area()} cone_2 volume is: {cone_1.get_volume()}")


C = Cone(4,10,10.77,"red",True)
print(C.get_volume())
