from random import randint
lista = [randint(0, 10) for a in range(1, 11)]
# Imprime a lista completa
print(lista)
# Imprime a posição do valor 10
print(f'Valor [10] encontrado na posição {lista.index(10)}.' if 10 in lista else 'Não encontrado')
