# Crie uma função para desenhar uma linha, usando o caractere '_'.
# O tamanho da linha deve ser definido na chamada da função.


def linha(tam=1):
    """
    -> Desenha uma linha na tela de tamanho definido pelo usuário.
    :param tam: Tamanho da linha a ser desenhado.
    :return: [print] Uma linha de tamanho definido pelo usuário. [Default = 1]
    """
    print('_' * tam)


linha(10)
