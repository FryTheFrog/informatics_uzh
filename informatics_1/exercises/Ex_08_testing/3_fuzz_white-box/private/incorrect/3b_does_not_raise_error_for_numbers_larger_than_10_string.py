#!/usr/bin/env python3
# Hint: Your tests do not detect a missing ValueError for string numbers larger than 10.

def calculate_factorial(inp):

    if inp is None:
        return None

    if type(inp) == int:
        if inp > 10:
            raise ValueError("ValueError: number negative")

    try:
        inp = int(inp)
    except:
        raise TypeError("TypeError: string")

    if inp < 0:
        raise ValueError("ValueError: number negative")

    output_answers = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    if inp <= 10:
        return output_answers[inp]
    else:
        return 100