from math import sqrt
A = float(input("Informe o quociente 'A' da equação do segundo grau: "))
B = float(input("Informe o quociente 'B' da equação do segundo grau: "))
C = float(input("Informe o quociente 'C' da equação do segundo grau: "))
delta = B*B -(4*A*C)
if delta < 0:
    print("Não existe raiz real.")
else:
    if delta == 0:
        raiz = -B/2*A
        print("A equacao aprensenta apenas 1 raiz: {}".format(raiz))
    else:
        r1 = ((-B)-sqrt(delta))/2*A
        r2 = ((-B)+sqrt(delta))/2*A
        print("A equacao aprensenta duas raízes reais: {} e {}".format(r1, r2))
