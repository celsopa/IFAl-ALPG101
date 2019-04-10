n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))
n3 = int(input("Digite o terceiro número "))
n4 = int(input("Digite o quarto número "))
numeros = [n1, n2, n3, n4]
print("São divisiveis por 2: ", end="")
for n in numeros:

    if n % 2 == 0:
        print(n, end=" ")
print()
print("São divisiveis por 3: ", end="")
for n in numeros:
    if n % 3 == 0:
        print(n, end=" ")
