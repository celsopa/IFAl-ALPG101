A = int(input("Digite o primeiro número "))
B = int(input("Digite o segundo número "))
C = int(input("Digite o terceiro número "))
if A <= B and A <= C:
    if B<=C:
        print(A, B, C)
    else:
        print(A, C, B)
elif B <= A and B <= C:
    if A<=C:
        print(B, A, C)
    else:
        print(B, C, A)
elif C <= A and C <=B:
    if A<=B:
        print(C, A, B)
    else:
        print(C, B, A)
