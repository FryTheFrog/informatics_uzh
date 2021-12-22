from public.geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, side_length, color, filled):
        self.__side_length = side_length
        self.set_color(color)
        self.set_filled(filled)

    def get_side_length(self):
        return self.__side_length

    def get_area(self):
        area = 6 * pow(self.__side_length, 2)
        return round(area, 2)

    def get_volume(self):
        volume = pow(self.__side_length, 3)
        return round(volume, 2)
