#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def read_csv(path):
    res = []
    # implement this function
    with open(path, "r") as f:
        for line in f.readlines():
            line = line[:-1]
            if len(line) == 0:
                continue

            t = tuple(line.split(","))
            res.append(t)
    return res

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(read_csv("public/example.csv"))
