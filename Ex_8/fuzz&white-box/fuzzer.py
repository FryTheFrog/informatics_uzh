import random

min_length_global = 0
max_length_global = 5
char_start_global = 30
char_end_global = 65

def fuzzer(min_length, max_length, char_start, char_end):
    length = random.randrange(min_length, max_length + 1)
    string = ''
    for i in range(length):
        i = random.randrange(char_start, char_end + 1)
        string += chr(i)
    print(string)
    return string

def calculate_factorial(inp):
    # validate input
    if inp == None: return None
    elif type(inp) == str:
        try: int(inp)
        except: raise TypeError('TypeError: string')
        else: inp = int(inp)
    if inp < 0: raise ValueError('ValueError: number negative')
    if inp > 10: raise ValueError('ValueError: number too large')

    # calculate
    def calc(inp):
        if inp == 0: return 1
        if inp == 1: return inp
        else: return inp * calc(inp - 1)
    
    return calc(inp)

def run(trials):
    val = []
    for i in range(trials):
        try:
            fuzz = fuzzer(min_length_global, max_length_global, char_start_global, char_end_global)
            calculate_factorial(fuzz)
        except ValueError as msg: fail = 1; i = str(msg)
        except: fail = 1; i = "Other error"
        else: fail = 0; i = ''
        val.append((fail, i))
    return val

print(run(1))
print(calculate_factorial('baum'))