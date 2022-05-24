# First Number
num1 = 1
# Second Number
num2 = 28

def isFriendlyPair():

    # The sum of divisors of num1
    teta1 = 0
    # The sum of divisors of num2
    teta2 = 0

    # Division of teta1 by num1 . teta1 / num1
    abundancy1 = 0 

    # Division of teta2 by num2 . teta2 / num2 
    abundancy2 = 0

    # Check if num1 and num2 are natural numbers and they are not the same. 
    # If conditions are not met return Invalid
    if num1 < 1 or num2 < 1 or num1 == num2 or not isinstance(num1, int) or not isinstance(num2, int):
        return "Invalid"
    else :
        # Find divisors of num1, calculate their sum and set it to teta1
        for x in range(1,num1+1):
            if num1%x==0:
                teta1 = teta1 + x
        
        # Calculate abundancy of number 1 by dividing teta1 by number 1
        abundancy1 = teta1 / num1 

        # Find dividers of num2, calculate their sum and set it to teta2
        for x in range(1,num2+1):
            if num2 % x==0:
                teta2 = teta2 + x
       
        # Calculate abundancy of number 2 by dividing teta1 by number 2
        abundancy2 = teta2 / num2

        # If both abundancies are equal num1 and num2 are friendly pairs so return True. 
        # If they are different return False since numbers are not friendly pairs
        if abundancy1 == abundancy2:
            return True 
        else :
            return False