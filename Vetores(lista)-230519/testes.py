def soma(x, y):
    total = x + y
    print("Total soma = ", total)


# programa principal
total = 10
soma(3, 5)
print("Total principal = ", total)


print('*'*40)
print('Variavel Global abaixo:')


def soma(x, y):
    global tot
    tot = x + y
    print("Total soma = ", tot)


# programa principal
global tot
tot = 10
soma(3, 5)
print("Total principal = ", tot)
