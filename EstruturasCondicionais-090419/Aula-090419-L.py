nome = input("Digite seu nome: ").title()
sexo = input("Digite seu sexo [M/F]: ").lower()[0]
if sexo == 'm':
    print("Ilmo. Sr. {}.".format(nome))
elif sexo == 'f':
    print("Ilma. Sra. {}.".format(nome))
else:
    print("Sexo Inválido.")