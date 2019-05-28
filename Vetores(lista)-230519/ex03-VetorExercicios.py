from random import randint
lista = [randint(1, 80) for a in range(1, 81)]
menor = pos = 0
print(lista)
for e in range(0, len(lista)):
    if e == 0:
        menor = lista[e]
        pos = e
    else:
        if lista[e] < menor:
            menor = lista[e]
            pos = e
print(f'O menor valor é {menor} e seu índice é {pos}.')
