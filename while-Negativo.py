#Crie um algoritmo que leia um numero diferente de zero e diga se este numero é positivo ou negativo

pergunta=1
while pergunta == 1:
    num = int(input("Digite um numero diferente de zero "))
    if num !=0:
        if num > 0:
            print("Esse número é positivo")
        else:
            print("Esse número é negativo")
    else:
        print("Digite um numero diferente de zero ")
    pergunta=int(input("Deseja perguntar novamente?\n 1 - Sim \n 2 - Não\n "))
