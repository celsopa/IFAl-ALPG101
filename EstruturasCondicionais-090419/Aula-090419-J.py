n = int(input("Digite um número entre 1 e 9: "))
if n < 1:
    print("O número '{}' é menor que 1. Está fora da faixa permitida.".format(n1))
elif n > 9:
    print("O número '{}' é maior que 9. Está fora da faixa permitida.".format(n1))
else:
    print("O número '{}' está dentro da faixa permitida.".format(n1))