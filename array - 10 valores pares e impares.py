#Faça um algoritmo que leia 10 valores do tipo inteiro e armazene-os em um vetor.
#A seguir, o algoritmo deverá informar:
#1 - todos os numeros pares que existem no vetor
#2 - o menor e o maior valor existente no vetor
#3 - quantos dos valores do vetor sao maiores que a media desses valores

lista = []
soma=0
cont=0
media=0
cont2=0
for x in range(5):
    lista.append(int(input("Digite um numero da lista: ")))
for x in range(5):
    if lista[x]%2==0:
        print("os numeros pares são ", lista[x])
for x in range(5):
    soma=soma+lista[x]
media = soma/5
print(media)
if lista[x] >= media:
    cont+=1
print("primeiro contador", cont)
for x in range(5):
    if lista[x] >= media:
        cont2+=1
print("segundo contador ", cont2)
maior=lista[0]
menor=lista[0]
for x in range(5):
    if lista[x] > maior:
        maior=lista[x]
for x in range(5):
    if menor[x]>menor:
        menor=menor[x]
