# This is how it could work in Python

rows = 5                        # instead of building up a string and
s = ""                          # and printing it as whole, just print it
                                # part by part
 
for i in range(rows + 1):
    for _ in range(rows - i):
        s += " "
    count = 0
    for j in range(2 * i - 1):
        if j <= i - 1:
            s += str(i + j)
        else:
            count += 1
            s += str(i + j - 2 * count)
    s += "\n"
    count = 0
print(s)
