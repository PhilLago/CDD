Av1 = float(input("Digite a nota da primeira avaliação: "))
while Av1<0 or Av1>10:
    print("Nota Inválida")
    Av1 = float(input("Digite a nota da primeira avaliação: "))
Av2 = float(input("Digite novamente a nota da segunda avaliação "))
while Av2<0 or Av2>10:
    print("Nota Inválida")
    Av2 = float(input("Digite novamente a nota da segunda avaliação: "))
print("A média do aluno é de", (Av1+Av2)/2)
