#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]

def get_possible_nrs(n):
    possible_nrs = []
    for pos in range(2, 10):
        for i in range(10):
            possible_nr = n[:pos] + str(i) + n[pos:]
            possible_nrs.append(possible_nr)
    possible_nrs_for_juliet = []
    for nr in possible_nrs:
        if nr in wa_nrs and nr not in possible_nrs_for_juliet:
            possible_nrs_for_juliet.append(nr)
    
    return possible_nrs_for_juliet

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))
