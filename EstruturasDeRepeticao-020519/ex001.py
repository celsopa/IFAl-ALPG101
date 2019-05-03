# 1) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.

print("="*40)
print(f'{"TABUADA DE MULTIPLICACAO":^40}')
print("="*40)
n = int(input('Informe o número desejado: '))
print("-"*40)
print(f"Tabuada de {n}:")
for x in range(1, 11):
    print(f"{n} x {x:>2} = {n*x:>2}")