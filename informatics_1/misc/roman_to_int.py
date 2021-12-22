# converts a roman number to an integer


def roman_to_int(roman: str) -> int:
    romdict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(roman)):
        if i + 1 < len(roman) and romdict.get(roman[i]) < romdict.get(roman[i + 1]):
            res -= romdict.get(roman[i])
        else:
            res += romdict.get(roman[i])
    return res


roman_num = "MCMXCIV"
print(roman_to_int(roman_num))
