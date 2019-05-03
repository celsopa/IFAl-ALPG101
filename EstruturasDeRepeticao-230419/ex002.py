# 2) Elaborar um programa que apresente no final o somatório dos valores pares existentes
# na faixa de 1 até 500.

soma = 0
for x in range(0, 501, 2):
    soma += x
print(f'O somatório dos números pares entre 1 e 500 é {soma}')
