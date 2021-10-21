a = 8
b = 12

def absolute_value(a):
    if a < 0: return -a
    else: return a

def gcd(a, b):
    a, b = absolute_value(a), absolute_value(b)
    if a == 0 and b == 0:
        return None
    if b == 0:
        return a
    return gcd(b, a % b)

print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")