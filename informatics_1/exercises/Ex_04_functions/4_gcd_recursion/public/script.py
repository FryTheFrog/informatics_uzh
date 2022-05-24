#!/usr/bin/env python3

import os

def absolute_value(a):
    if a < 0: return -a
    else: return a

def gcd(a, b):
    a = absolute_value(a)
    b = absolute_value(b)
    if a == 0 and b == 0:
        return None
    if b == 0:
        return a
    return gcd(b, a % b)

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 33
b = 17
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")