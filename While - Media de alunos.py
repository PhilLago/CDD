Alunos = int(input("Qual é o número de alunos da sala?: "))
soma = 0
x = 1
while x <=Alunos:
    Nota = float(input("Qual é a nota do aluno? "))
    soma= soma+Nota
    x+=1
Media = soma/Alunos
print("A média da nota dos alunos é de: ", Media)
