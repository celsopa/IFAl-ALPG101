base = int(input())
exp = int(input())
res = 1
while exp > 0:
    res *= base
    exp -=1
print(res)
