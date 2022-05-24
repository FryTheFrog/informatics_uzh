#!/usr/bin/env python3

# absolute value function
def absolute_value(a):
    if a < 0:
        return -a
    return a


def gcd(a, b):
    # handle zero-division error
    if a == 0 and b == 0:
        return None
    else:
        if a == 0 or b == 0:
            return absolute_value(a) if a != 0 else absolute_value(b)
        else:
            # ensure input is positive
            a = absolute_value(a)
            b = absolute_value(b)

            # swap values
            if a < b:
                a, b = b, a

            # base case
            if a % b == 0:
                return b

            # recursive case
            return gcd(b, a % b)

