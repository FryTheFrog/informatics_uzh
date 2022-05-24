#!/usr/bin/env python3
# Hint: Your test do not detect that None is not returned when inp is equal to None.

def calculate_factorial(inp):

    try:
        inp = int(inp)
    except:
        raise TypeError("TypeError: string")

    if inp < 0:
        raise ValueError("ValueError: number negative")

    if inp > 10:
        raise ValueError("ValueError: number too large")

    if inp == 0:
        return 1
    factorial = 1
    for i in range(1, inp + 1):
        factorial *= i
    return factorial