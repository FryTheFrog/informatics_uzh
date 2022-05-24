#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 10

# build a string 
def build_string_pyramid():

    # init for h = 0
    s = ""

    # build the first half of the pyramid
    for i in range(1, h + 1):
        for j in range(1,i+1):
            s += str(j)
            if j < i:
                s += "*"
        s += "\n"
    
    # build the second half of the pyramid
    for i in range(h-1, 0, -1):
        for j in range(1,i+1):
            s += str(j)
            if j < i:
                s += "*"
        s += "\n"

    return s

# printing the pyramid string to console
print(build_string_pyramid())