pwd = 'abAB12++'

def pwd_check():
    char = ['+', '-', '*', '/']
    lowcount = 0
    upcount = 0
    digcount = 0
    charcount = 0
    validity = False
    for i in pwd: 
        if i.islower():
            lowcount += 1
        if i.isupper():
            upcount += 1
        if i.isdigit():
            digcount += 1
        if i in char:
            charcount += 1
    if lowcount >= 2 and upcount >= 2 and digcount >= 2 and charcount >= 2:
        if len(pwd) >= 8 and len(pwd) <= 16:
            validity = True

    for i in pwd:
        if not i.isalnum() and i not in char:
            validity = False
    return validity

print(pwd_check())