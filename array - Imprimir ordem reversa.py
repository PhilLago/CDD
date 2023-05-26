#escreva um algoritmo que solicite ao usuario a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
#apos exibir essa lista, o programa deve mostrar tbm os nomes na ordem inversa em que o usuario os digitou, por linha

lista=[]
for x in range(5):
    lista.append(input("Digite os nomes da lista: "))
for y in range(5):
    print(lista[y])
for z in range(4,-1,-1):
    print(lista[z])
#for x in range 5:
#    print