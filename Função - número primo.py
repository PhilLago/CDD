#faça uma função que recebe um número como paramentro e verifique se este numero é primo
def calcularPrimo(num):
    cont=0
if num==1:
    print(num," não é primo")
    return
    for x in range(1, num+1):
        if num%x==0:
            cont+=1
    if cont==2:
        print(num, "é primo")
    else:
        print(num, "não é primo")
#crian os Return