from public.geometric_object import GeometricObject


class Cylinder(GeometricObject):

    def __init__(self, radius, height, color, filled):
        self.__radius = radius
        self.__height = height
        self.__PI = 3.14
        self.set_color(color)
        self.set_filled(filled)

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def get_area(self):
        area = 2*self.__PI * pow(self.__radius, 2) + 2 * \
            self.__PI * self.__radius * self.__height
        return round(area, 2)

    def get_volume(self):
        volume = self.__PI*pow(self.__radius, 2)*self.__height
        return round(volume, 2)
