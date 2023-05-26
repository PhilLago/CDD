frase=input("digite a frase:")
def contador(t):
    cont=0
    for x in frase:
        if x in "AaEeIiOoUu":
            cont+=1
    print(cont)

contador(frase)