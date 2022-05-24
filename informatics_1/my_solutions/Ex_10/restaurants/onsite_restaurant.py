from restaurant import Restaurant


class OnsiteRestaurant(Restaurant):
    def __init__(self, name, cuisine_type, num_tables, is_open=False):
        super().__init__(name, cuisine_type, is_open)
        self.__num_tables = num_tables
        self.__available_tables = num_tables

    def occupy_table(self):
        if self.__available_tables < 1:
            raise Warning("no tables available")
        else:
            self.__available_tables -= 1

    def free_table(self):
        if self.__available_tables == self.__num_tables:
            raise Warning("all tables are free")
        else:
            self.__available_tables += 1

    def get_available_tables(self):
        return self.__available_tables
