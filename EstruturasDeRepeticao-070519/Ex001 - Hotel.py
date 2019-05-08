from random import randint

i = 1
tot = 0
hotel = []
for x in range(30):
    diarias = randint(1, 30)
    if diarias < 15:
        ts = diarias * 4
    elif diarias == 15:
        ts = diarias * 3.6
    else:
        ts = diarias * 3
    hotel.append([diarias, ts])
print(f"""{'-={{ HOTEL CALIFORNIA }}=-':^46} 
VALOR DA DIÁRIA: R$50,00 (cinquenta reais)
TAXA DE SERVIÇO: de R$3,00 a 4,00 / diária
{'-'*46}""")
for q in hotel:
    print(f"""Quarto {i}:
    Diárias: {q[0]}
    Taxa de Serviço: R${q[1]:.2f}
    TOTAL DA CONTA: R${50*q[0] + q[1]:.2f}
    """)
    i += 1
    tot += (50*q[0] + q[1])
print(f"TOTAL RECEBIDO PELO HOTEL: R$ {tot:.2f}")