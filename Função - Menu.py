#1-Somar
#2-Subtrair
#3-multiplicar
#4-dividir
#5-sair

def somar(n1,n2):
    soma=n1+n2
    print(soma,"\n")
def subtrair(n1,n2):
    subtracao=n1-n2
    print(subtracao,"\n")
def multiplicar(n1,n2):
    multiplicacao=n1*n2
    print(multiplicacao,"\n")
def dividir(n1,n2):
    divisao=n1/n2
    print(divisao,"\n")

menu=1
while menu >=1 and menu <=5:
    menu = int(input("Digite o número da operação:\n\n1-Somar \n2-Subtrair \n3-multiplicar \n4-dividir \n5-sair \n"))
    if menu==5:
        print("Programa Encerrado")
        break

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if menu ==1:
        somar(n1,n2)

    elif menu==2:
        subtrair(n1,n2)

    elif menu==3:
        multiplicar(n1,n2)
    else:
        dividir(n1,n2)

