#!/usr/bin/env python3

class Fridge:

    def __init__(self):
        self.__content = []

    def store(self, item):
        self.__content.append(item)

    def take(self, item):
        if item not in self.__content:
            raise Warning()
        self.__content.remove(item)
        return item

    def find(self, name):
        for i in self:
            if i[1] == name:
                return i
        return None

    def take_before(self, date):
        items = []
        for i in self.__content:
            if i[0] < date:
                self.__content.remove(i)
                items.append(i)
        return items

    def __iter__(self):
        return iter(sorted(self.__content))

    def __len__(self):
        return len(self.__content)
