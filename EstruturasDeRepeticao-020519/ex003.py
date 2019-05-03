# 3) Escreva um programa que apresente a série de Fibonacci até o décimo quinto termo.
# A série de Fibonacci é formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., etc.
# Esta série se caracteriza pela soma de um termo atual com o seu anterior subsequente,
# para que seja formado o próximo valor da sequência.
# Portanto começando com os números 1, 1 o próximo termo é 1+1=2, o próximo é 1+2=3,
# o próximo é 2+3=5, o próximo 3+5=8, etc.

tA = 0
tS = 1
atual = 1
print("Os 15 primeiros números da sequencia de Fibonacci:")
print(atual, end=" | ")
for x in range(14):
    atual = tA + tS
    if x != 14:
        print(atual, end=" | ")
    else:
        print(atual)
    tA = tS
    tS = atual
