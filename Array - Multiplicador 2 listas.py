#Ler um vetor A de 10 números. Logo em seguida, ler mais um numero e guardar em uma variavel X
#Armazenar em um vetor M o resultado de cada elemento em A multiplicado pelo valor X.
#Logo após, imprimir o vetor M

a=[]
m=[]
quantidade = int(input("Digite a quantidade: "))
for x in range(quantidade):
    a.append(int(input(("Digite 10 números: "))))
multiplicador = int(input("Qual é o multiplicador? "))
for y in range(quantidade):
    m.append(a[y]*multiplicador)
print(a)
print(multiplicador)
print(m)