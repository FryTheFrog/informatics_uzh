# check if a number is a palindrome


def reverse_num(num: int) -> int:
    r = 0
    while num > 0:
        r *= 10
        r += num % 10
        num //= 10
    return r


def palindrome(num: int) -> bool:
    if num == reverse_num(num):
        return True
    else:
        return False


n = 12321
print(palindrome(n))
