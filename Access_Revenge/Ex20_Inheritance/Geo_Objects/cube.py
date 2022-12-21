from geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, side_length, color, filled):
        super().__init__(color, filled)
        self.__side_length = side_length
        

    def get_side_length(self):
        return self.__side_length

    def set_side_length(self, side_length):
        side_length = self.__side_length

    def get_area(self):
        out = 6*(self.__side_length**2)
        return round(out, 2)

    def get_volume(self):
        out = self.__side_length**3
        return round(out, 2)
