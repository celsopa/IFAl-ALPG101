# Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo.
# A função deve imprimir todos os elementos da lista numerando-os.


def detalhe(lista=None):
    """
    -> Imprime os elementos da lista com indicação de seus respectivos índices.
    :param lista: uma lista. [Default = lista vazia]
    :return: [print] O índice e o respectivo elemento.
    """
    if lista is None:
        lista = []
    for i in range(len(lista)):
        print(f'No índice {i} temos o elemento: {lista[i]}')


detalhe(['a', 'b', 'c'])
