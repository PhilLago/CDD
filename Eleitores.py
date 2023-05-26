#escreva um algoritmo para ler o número total de eleitores de um municipio, o numero de votos brancos e nulos e invalidos
#Calcular e escrever o percentual que cada um representa em relação ao total de eleitores

total=int(input("Qual é o número total de eleitores? "))
votosBrancos=int(input("Qual é o número total de votos brancos? "))
votosNulos=int(input("Qual é o número total de votos nulos? "))
votosValidos=total-votosNulos-votosBrancos

totalBrancos=(votosBrancos*total)/100
totalNulos=(votosNulos*total)/100
totalValidos=(votosValidos*total)/100

print(totalBrancos,"%\n",totalNulos,"%\n",totalValidos,"%")