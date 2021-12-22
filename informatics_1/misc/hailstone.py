# Hailstone Sequence
# Write a function that, starting from an arbitrary positive integer n, generates a list of integers.
# The list should start with n, followed by a sequence, which is generated according to two rules:
#   - if the current element is even, divide it by 2 to generate the next element
#   - if the current element is odd, multiply it by 3 and add 1 to generate the next element
# End the sequence once you reach a value of 1 to prevent an endless continuation
# (1, 4, 2, 1, ...). This resulting sequence is called the hailstone sequence.


def hailstone(n: int) -> list:
    res_list = []
    res_list.append(n)
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        res_list.append(n)

    return res_list


n = 6
print(hailstone(n))
