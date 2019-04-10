n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
n4 = float(input("Informe a quinta nota: "))
media = (n1+n2+n3+n4)/4
if media >= 5:
    print("Aluno aprovado com média {}".format(media))
else:
    print("Aluno reprovado. Média: {}".format(media))