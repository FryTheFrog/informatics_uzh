class Fridge:
    def __init__(self):
        self.__inv = []
        self.__idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__idx < len(self.__inv):
            res = self.__inv[self.__idx]
            self.__idx += 1
            return res
        else: raise StopIteration

    def __len__(self):
        return len(self.__inv)

    def store(self, item):
        self.__inv.append(item)
        self.__inv.sort()

    def find(self, name):
        for i in self.__inv:
            if name.lower() in i[1].lower():
                return i

    def take(self, item):
        if item in self.__inv:
            self.__inv.remove(item)
            return item
        else: raise Warning('No such item in fridge')

    def take_before(self, date):
        removed = []
        for i in self.__inv:
            if i[0] < date:
                removed.append(i)
        self.__inv = [i for i in self.__inv if i not in removed]
        return removed