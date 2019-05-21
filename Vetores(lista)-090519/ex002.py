# 2 – Gere uma lista de contendo os múltiplos de 3 entre 1 e 60.

lista = []
for i in range(3, 61, 3):
    lista.append(i)
print(f'Lista: {lista}')