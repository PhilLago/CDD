Senha = input("Qual é a sua senha?: ")
Correto = "1234"
Tentativas = 3
while Correto != Senha:
    Tentativas=-1
    print("A senha está incorreta, você tem", Tentativas, "restantes")
    Senha = input()
    if Tentativas >=0:
        print("Senha bloqueada")
        break
else:
    print("Acesso liberado")