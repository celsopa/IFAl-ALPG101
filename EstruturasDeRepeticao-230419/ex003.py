# 3) Apresentar todos os números divisíveis por 4 que sejam menores que 200. Para verificar
# se o número é divisível por 4, efetuar dentro da malha a verificação lógica desta condição
# com a instrução se, perguntando se o número é divisível; sendo, mostre-o; não sendo,
# passe para o próximo passo. A variável que controlará o contador deve ser iniciada com o
# valor 1.

for x in range(1, 201):
    if x == 200:
        print(x)
    elif x % 4 == 0:
        print(x, end="|")