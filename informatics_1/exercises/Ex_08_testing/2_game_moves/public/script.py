#!/usr/bin/env python3

def move(state, direction):
    pass


# The following line calls the function and prints the return
# value to the Console.
s1 = (
    "#####   ",
    "###    #",
    "#   o ##",
    "   #####"
)
s2 = move(s1, "right")

print("= New State =")
print("\n".join(s2[0]))
print("\nPossible Moves: {}".format(s2[1]))
