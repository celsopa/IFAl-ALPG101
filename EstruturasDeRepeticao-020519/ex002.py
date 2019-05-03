# 2) Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100)

from time import sleep
print("Somando os 100 primeiros números inteiros...")
tot = 0
for x in range(1, 101):
    tot += x
    print(x, end="") if x != 100 else print(x)
    sleep(0.1)
    if x != 100:
        print('+', end="")
    if x % 25 == 0 and x != 100:
        print()
    else:
        print(end='')
print(f'O total é {tot}')
