#!/usr/bin/env python3
# Hint: Your tests do not detect a missing ValueError for negative string numbers as inp.

def calculate_factorial(inp):

    if inp is None:
        return None

    if type(inp) == int:
        if inp < 0:
            raise ValueError("ValueError: number negative")

    try:
        inp = int(inp)
    except:
        raise TypeError("TypeError: string")

    if inp > 10:
        raise ValueError("ValueError: number too large")

    if inp == 0:
        return 1
    factorial = 1
    for i in range(1, inp + 1):
        factorial *= i
    return factorial