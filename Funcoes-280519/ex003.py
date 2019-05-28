# Crie uma função que receba como parâmetro uma lista com valores numéricos e retorne a média desses valores.


def media_lista(lista=None):
    """
    -> Calcula a média dos elementos de uma lista.
    :param lista: Uma lista contendo números inteiros.
    :return: A média dos elementos da lista.
    """
    if lista is None:
        return None
    media = 0
    for num in lista:
        media += num
    media /= len(lista)
    return media


print(media_lista([1, 2, 3, 4, 5, 6, 7, 8, 9]))
