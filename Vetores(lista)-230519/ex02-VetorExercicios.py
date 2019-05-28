from random import randint
lista = [randint(0, 5) for a in range(1, 101)]
print(lista)
lista = [a if a != 0 else 1 for a in lista]
print(lista)
