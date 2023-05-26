Mes = int(input("Digite o mês do ano: "))
if Mes >= 1 and Mes <= 12:
    if Mes == 1:
        print("O mês é Janeiro!")
    elif Mes == 2:
        print("O mês é Fevereiro")
    elif Mes == 3:
        print("o mês é Março")
    elif Mes == 4:
        print("O mês é Abril")
    elif Mes == 5:
        print("o mês é Maio")
    elif Mes == 6:
        print("O mês é Junho")
    elif Mes == 7:
        print("o mês é Julho")
    elif Mes == 8:
        print("O mês é Agosto")
    elif Mes == 9:
        print("o mês é Setembro")
    elif Mes == 10:
        print("O mês é Outubro")
    elif Mes == 11:
        print("o mês é Novembro")
    else:
        print("O mês é Dezembro")
else:
    print("Não é um mês")
