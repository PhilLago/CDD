n1=int(input("Digite um número: "))
def sequenciar(n1):
    for x in range(1,n1+1):
        for y in range(1,x+1):
            print(y, end="")
        print()

sequenciar(n1)