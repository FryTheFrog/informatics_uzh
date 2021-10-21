a, b = [1, 2, 3], [4]

def merge(a, b):
    mergelist = []
    if len(a) > len(b):
        long = len(a)
    else : long = len(b)
    if a == [] or b == []: return []
    for i in range(long):
        if i < len(a) and i < len(b):
            mergelist.append((a[i], b[i]))
        elif i >= len(a):
            mergelist.append((a[-1], b[i]))
        elif i >= len(b):
            mergelist.append((a[i], b[-1]))

    return mergelist

print(merge(a, b))