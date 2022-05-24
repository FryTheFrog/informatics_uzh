#!/usr/bin/env python3
# Sample Solution
import random

min_length_global = 1
max_length_global = 1
char_start_global = 65
char_end_global = 65

def fuzzer(min_length, max_length, char_start, char_end):
    string = ""
    string_length = random.randrange(min_length, max_length + 1)
    for _ in range(0, string_length):
        string += chr(random.randrange(char_start, char_end + 1))
    return string


def calculate_factorial(inp):

    if inp is None:
        return None
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


def run(trials):
    l = []
    for _ in range(trials):
        inp = fuzzer(min_length_global, max_length_global, char_start_global, char_end_global)
        try:
            calculate_factorial(inp)
        except ValueError as e:
            l.append((1, str(e)))
        except:
            l.append((1, "Other error"))
        else:
            l.append((0, ""))
    return l
