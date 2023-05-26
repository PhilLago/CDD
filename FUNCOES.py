def somar(*args):
    total=0
    for x in args:
       total+=x
    return total
def subtrair(*args):
    total = 0
    for x in args:
        total-= x
    return total
def multiplicar(*args):
    total = 1
    for x in args:
        total*=x
    return total
def dividir(n1,n2):
    return n1/n2
def sequenciar(n1):
    for x in range(1,n1+1):
        for y in range(1,x+1):
            print(y, end="")
        print()
def estoque(nome,quantidade,valor):
    return nome,quantidade*valor

def inverter(texto):
    cont=0
    for x in texto:
        if x != " ":
            cont+=1
    return cont,texto[::-1]


def calcularPrimo(num):
    cont=0
    for x in range(1, num+1):
        if num%x==0:
            cont+=1
    print(cont)
    if cont==2:
        print(num, "é primo")
    else:
        print(num, "não é primo")
