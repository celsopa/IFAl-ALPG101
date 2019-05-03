# 5) Elaborar um programa que efetue a leitura de 15 valores numéricos inteiros e no final
# apresente o total do somatório da fatorial de cada valor lido.

x = 3
somaFatorial = 0
fatorial = []
while x > 0:
    x -= 1
    n = int(input("Informe um número para que seja calculado seu fatorial: "))
    fat = 1
    for y in range(1, n+1):
        fat *= y
    somaFatorial += fat
    fatorial.append((n, fat))
for f in fatorial:
    print(f"{f[0]}! = {f[1]:}")
print(f"O somatório de todos os fatoriais é: {somaFatorial}")
