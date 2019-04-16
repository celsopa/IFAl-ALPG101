i = 1
soma = 0
n = 50
while n <=70:
    if n%2==0:
        soma += n
        i+=1
    n +=1
print("SOMA: {}.\nMEDIA: {}.".format(soma, int(soma/i)))