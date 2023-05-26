# Faça um código para ler X números e armazenar em um vetor. Após a leitura total dos X números,
# o código escreve esses X números lidos na ordem inversa

vetor=[]
quantidade = int(input("Digite a quantidade de números: "))
for x in range(quantidade):
    vetor.append(input("Digite os números: "))
for y in range(quantidade-1,-1 ,-1):
    print(vetor[y])