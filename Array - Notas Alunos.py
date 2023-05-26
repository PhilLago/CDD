#Escreva um código que permita a leitura das notas de uma turma de 5 alunos  e guarde num vetor,
#calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada
#escrever a média da turma e o resultado da contagem

nota=[]
soma=0
cont=0
quantidade = int(input("Digite a quantidade dos alunos "))
for x in range(quantidade):
    nota.append(float(input("Digite as notas dos alunos ")))
for y in range(quantidade):
    soma+=nota[y]
media = soma/quantidade
for z in range(quantidade):
    if nota[z] >= media:
        cont+=1
print("A media da turma foi de ", media)
print("E o número de alunos acima da media foi de ", cont)
