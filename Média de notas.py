# Faça um algoritmo que receba 2 notas e calcule a média aritmetica

medias=[]
pergunta="S"
while pergunta == "S":
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print(media)
    medias.append(media)
    if media >= 7:
        print("Aprovado")

    elif media >= 4:
        print("Recuperação")

    else:
        print("Reprovado")

    pergunta = input("Você quer fazer um novo calculo? ")
    if pergunta == "N":
        print("Programa encerrado")
        break