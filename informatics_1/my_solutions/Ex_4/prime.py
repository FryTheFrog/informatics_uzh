x = int(input("Enter number: "))

flag = False

if x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            flag = True
            break
else:
    flag = True

if flag:
    print("no")
else:
    print("yes")
