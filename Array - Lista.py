#Perguntar ao usuário quantos alunos tem na sala e criar um array,
#unidimensional(vetor com o nome de todos os alunos da sala

alunos=[]
n = int(input("Digite a quantidade de alunos "))
for x in range(n):
    alunos.append(input("Digite o nome do aluno "))
pesquisa = input("Digite o nome que você quer pesquisar ")
cont=0
for y in range(n):
    if pesquisa == alunos[y]:
        print(y, alunos[y])
    else:
        cont+=1
if cont == n:
    print("Aluno não consta na lista")




    #print(alunos[y], y)
