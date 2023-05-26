#Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente,
#após complementar a digitação, imprimir, nome, senha e posição dos dados no array

nome=[]
senha=[]
cont=0
for x in range(3):
    nome.append(input("Digite o nome do usuário "))
    senha.append(input("Digite a senha do usuário "))
#for y in range(5):
#    print(y,nome[y],senha[y])
nome2=input("Qual é o seu usuário? ")
senha2=input("Qual é a sua sennha? ")
for y in range(3):
    if nome2 == nome[y] and senha2 == senha[y]:
        print("Login efetuado com sucesso")
        break
    else:
        cont+=1
if cont==3:
    print("Usuário ou senha inválidos")
