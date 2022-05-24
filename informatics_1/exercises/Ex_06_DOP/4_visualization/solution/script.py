#!/usr/bin/env python3

def visualize(records):
    grouped = {
        1: [],
        2: [],
        3: []
    }
    for r in records[1]:
        grouped[r[1]].append(r)

    total = len(grouped[1]) + len(grouped[2]) + len(grouped[3])

    out = ""
    for idx, t_class in [(1, "1st Class"), (2, "2nd Class"), (3, "3rd Class")]:
        g_total = len(grouped[idx])
        g_alive = 0
        for r in grouped[idx]:
            if r[0]:
                g_alive += 1
        out += "== {} ==\n".format(t_class)
        out += bar("Total", g_total, total)
        out += bar("Alive", g_alive, g_total)

    return out

def bar(title, a, b):
    perc = round(100*a/b, 1)
    num_symbols = round(perc/5)
    num_spaces = 20-num_symbols
    return "{} |{}{}| {}%\n".format(title, num_symbols*"*", num_spaces*" ", perc)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(visualize((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (True, 2, 'Flunky Mr Hazelnut', 'female', 18, 51.2),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
    ]
)))
