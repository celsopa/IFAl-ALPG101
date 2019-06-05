gabarito = input()
classe = []
somaNotas = 0
while True:
    nome = input()
    if nome in "sair":
        break
    gabAluno = input()
    nota = 0
    for x in range(len(gabarito)):
        if gabarito[x] == gabAluno[x]:
            nota += 1
    classe.append((nome, nota))
    somaNotas += nota

media = somaNotas/len(classe)
qtdAcimaMedia = 0
maior = 0
alunoMaior = 'mior'

for x in range(len(classe)):
    if classe[x][1] > media:
        qtdAcimaMedia += 1
    if classe[x][1] > maior:
        maior = classe[x][1]

for x in classe:
    if x[1] == maior:
        alunoMaior = x[0]


print(qtdAcimaMedia)
print(alunoMaior)