#!/usr/bin/env python3

# play with this test list of Whatsapp numbers
wa_nrs = ["0781111119", "0792663913", "0792663139", "0792663193", "0781139022", "0764320165"]

def get_possible_nrs(n):

    n = "".join(n.split(" "))
    guess_phone = ""
    possible_juliet_nrs = []

    # append one digit at every location in the number
    for guess_idx in range(2, len(n) + 1):
        for guess_nr in range(10):
            guess_phone = n[:guess_idx] + str(guess_nr) + n[guess_idx:]
    
            # check whether number is in our list
            if guess_phone in wa_nrs and not guess_phone in possible_juliet_nrs:
                possible_juliet_nrs.append(guess_phone)
        
    return possible_juliet_nrs
    

print(get_possible_nrs("079266313"))
