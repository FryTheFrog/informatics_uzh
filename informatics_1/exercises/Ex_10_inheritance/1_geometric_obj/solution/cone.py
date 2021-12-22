from public.geometric_object import GeometricObject


class Cone(GeometricObject):

    def __init__(self, radius, vertical_height, slant_height, color, filled):
        self.__radius = radius
        self.__vertical_height = vertical_height
        self.__slant_height = slant_height
        self.__PI = 3.14
        self.set_color(color)
        self.set_filled(filled)

    def get_radius(self):
        return self.__radius

    def get_vertical_height(self):
        return self.__vertical_height

    def get_slant_height(self):
        return self.__slant_height

    def get_area(self):
        area = self.__PI * pow(self.__radius, 2) + self.__PI * \
            self.__radius*self.__slant_height
        return round(area, 2)

    def get_volume(self):
        volume = (self.__PI * pow(self.__radius, 2)
                  * self.__vertical_height) / 3
        return round(volume, 2)
