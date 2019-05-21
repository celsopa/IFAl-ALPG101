# 1 – Dada a lista L1 = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes
# informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

l1 = [5, 7, 2, 9, 4, 1, 3]
tamanho = maior = menor = soma = 0

# Encontra o tamanho e a soma dos valores da lista : l1 = [5, 7, 2, 9, 4, 1, 3]
for i in l1:
    tamanho += 1
    soma += i

# Percorre a lista para verificar qual o maior e o menor valor :l1 = [5, 7, 2, 9, 4, 1, 3]
for i in range(0, tamanho):
    if i == 0:
        maior = l1[i]
        menor = l1[i]
    else:
        if l1[i] > maior:
            maior = l1[i]
        if l1[i] < menor:
            menor = l1[i]

# Ordena a lista de forma crescente : l1 = [5, 7, 2, 9, 4, 1, 3]
troca = 1
listaCresc = l1[:]
while troca:
    troca = 0
    for i in range(0, len(listaCresc) - 1):
        if listaCresc[i] > listaCresc[i + 1]:
            listaCresc[i], listaCresc[i + 1] = listaCresc[i + 1], listaCresc[i]
            troca = 1

# Ordena a lista de forma decrescente : l1 = [5, 7, 2, 9, 4, 1, 3]
troca = 1
listaDecr = l1[:]
while troca:
    troca = 0
    for i in range(0, len(listaDecr) - 1):
        if listaDecr[i] < listaDecr[i + 1]:
            listaDecr[i], listaDecr[i + 1] = listaDecr[i + 1], listaDecr[i]
            troca = 1

print(f'Analisando a lista {l1}')
print(f'a) A lista tem {tamanho} elementos.')
print(f'b) O MAIOR valor da lista é {maior}.')
print(f'c) O MENOR valor da lista é {menor}.')
print(f'd) A soma dos elementos da lista {l1} é {soma}.')
print(f'e) Lista em ordem crescente: {listaCresc}')
print(f'f) Lista em ordem decrescente: {listaDecr}')
