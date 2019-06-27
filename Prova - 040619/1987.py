total = float(input().strip())
totalPago = 0

funcionarios = int(input().strip())
pagamentos = []
while funcionarios > 0:
    nome = input().strip()
    valor = float(input().strip())
    totalPago += valor
    pagamentos.append((valor, nome))
    funcionarios -=1

excedente = totalPago - total


pagamentos.sort(reverse=True)
print("{} pagou R$ {}".format(pagamentos[0][1], pagamentos[0][0]))
if excedente >= 0:
    print("Valor excedente: sobra R$ {}".format(excedente))
else:
    print("Valor insuficiente: falta R$ {}".format(-excedente))
