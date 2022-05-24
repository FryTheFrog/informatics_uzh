#!/usr/bin/env python3

def is_prime(n):
    if n == 1:
        return "1 is the multiplicative identity"
    for a in range(2, n):
        if n % a == 0:
            b = n // a
            return f"{n} is not a prime number ({a} * {b} = {n})"
    return f"{n} is prime"

