#!/usr/bin/env python3

pwd = "abc"


def is_valid():
    validity = True

    size = 0
    num_lower = 0
    num_upper = 0
    num_special = 0
    num_digits = 0

    allowed_special = "+-/*"
    for c in pwd:
        size += 1
        if c.isdigit():
            num_digits += 1
        elif c.islower():
            num_lower += 1
        elif c.isupper():
            num_upper += 1
        elif c in allowed_special:
            num_special += 1
        else:
            validity = False
    validity = validity and size >= 8 and size <= 16 and num_lower > 1 and num_upper > 1 and num_digits > 1 and num_special > 1
    return validity
