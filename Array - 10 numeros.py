#faça um codigo para ler um vetor de 30 numeros. Apos isto, ler mais um numero qualquer, calcular e escrever
#quantas vezes esse numero aparece no vetor

lista=[]
cont=0

for x in range(10):
    lista.append(input("digite um numero da lista "))
numero = input("Digite um numero ")
for x in range(10):
    if numero == lista[x]:
        cont+=1
print(lista[x],cont)