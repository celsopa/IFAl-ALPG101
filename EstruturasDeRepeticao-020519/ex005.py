# 5) Elaborar um programa que apresente como resultado o valor do fatorial
# dos valores ímpares situados na faixa numérica de 1 a 10.

print('Apresentando o fatorial dos númros ímpares situados entre 1 e 10:')

for x in range(1, 11, 2):
    fat = 1
    for y in range(1, x+1):
        fat *= y
    print(f'{x}! = {fat}')
