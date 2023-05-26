#Faça um algoritmo que leia a idade de uma pessoa expressa em anos meses e dias
# e escreva a idade dessa pessoa expressa apenas em dias. Considerar anos com 365 dias e mes com 30.

idade=int(input("Qual é a sua idade "))
mes=int(input("Qual mês você nasceu "))
dia=int(input("Qual dia você nasceu"))


resultado=(idade*365)+(mes*30)+dia
print(resultado)