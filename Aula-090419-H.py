n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))
n4 = int(input("Informe o quarto número: "))
n5 = int(input("Informe o quinto número: "))
numeros = [n1, n2, n3, n4, n5]
maior = n1
menor = n1
for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print("O maior numero digitado foi: {}.".format(maior))
print("O menor numero digitado foi: {}.".format(menor))