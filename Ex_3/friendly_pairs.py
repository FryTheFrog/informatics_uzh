num1 = 6
num2 = 28

def is_friendly_pair():
    if num1 == num2:
        return 'Invalid'
    if not isinstance(num1, int) or not isinstance(num2, int) or num1 < 1 or num2 <1:
        return 'Invalid'

    div1 = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            div1.append(i)

    div2 =[]
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            div2.append(i)
    
    if sum(div1)/num1 == sum(div2)/num2:
        return True
    else: return False


print(is_friendly_pair())