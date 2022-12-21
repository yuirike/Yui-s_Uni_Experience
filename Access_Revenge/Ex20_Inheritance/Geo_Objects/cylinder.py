from geometric_object import GeometricObject


class Cylinder(GeometricObject):

    def __init__(self, radius, height, color, filled):
        # GeometricObject.__init__(self, color, filled)
        super().__init__(color, filled)

        self.__radius = radius
        self.__height = height
        self.__PI = 3.14

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def get_area(self):
        out = 2*self.__PI*self.__radius*(self.__height+self.__radius)
        return round(out,2)

    def get_volume(self):
        out = self.__PI*(self.__radius**2)*self.__height
        return round(out,2)


