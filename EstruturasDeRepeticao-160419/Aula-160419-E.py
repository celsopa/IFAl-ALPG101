exp = 0
result = 1
i = 1
while exp <= 15:
    if exp == 0:
        print(1)
    elif exp ==1:
        print(3)
    else:
        while i <= exp:
            result *= 3
            i += 1
        print(result)
    exp += 1

