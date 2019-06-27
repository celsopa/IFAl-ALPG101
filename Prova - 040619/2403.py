n = int(input())
divisores = []
divisor = 2
maior = 0
lista = []

while n > 1:

    if n % divisor == 0:
        qtd = 0
        while n % divisor == 0:
            divisores.append(divisor)
            n = n / divisor
            qtd += 1
        else:
            lista.append((qtd, divisor))
    else:
        divisor += 1


lista.sort(reverse=True)

frequencia = lista[0][0]
maisFrequente = 9999999999999999
for l in lista:
    if l[0] == frequencia:
        maisFrequente = l[1]
        if l[1] < maisFrequente:
            maisFrequente = l[1]

print("mostFrequent: {}, frequency: {}".format(maisFrequente, frequencia))

# print("mostFrequent: {}, frequency: {}".format(lista[0][1], lista[0][0]))