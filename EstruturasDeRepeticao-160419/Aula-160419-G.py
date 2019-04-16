i = 1
n1 = 0
n2 = 1
n = 1
print(n, end=", ")
while i <=15:
    n = n1 + n2
    if i == 15:
        print(n, end=".")
    else:
        print(n, end=", ")
    n1 = n2
    n2 = n
    i +=1
