h = 5

def build_string_pyramid():
    hrange = range(1, h + 1)
    s = str()

    for j in hrange:
        for i in range(1, j + 1):
            s = s + str(i)
            if i < j:
                s = s + '*'
        s = s + '\n'

    for j in hrange:
        temprange = range(1, h - j + 1)
        for i in temprange:
            s = s + str(i)
            if i < h - j:
                s = s + '*'
        if j < h:
            s = s + '\n'

    return s

print(build_string_pyramid())