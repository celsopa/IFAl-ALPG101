n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
media = (n1+n2+n3+n4)/4
if media >= 7:
    print("Aluno aprovado com média {}".format(media))
else:
    nExame = float(input())
    media = (media+nExame)/2
    if media >= 5:
        print("Aluno aprovado em exame final. Media: {}".format(media))
    else:
        print("Aluno reprovado em exame final. Media: {}".format(media))
