a=[]
b=[]
c=[]
quantidade = int(input("Digite a quantidade: "))
for x in range(quantidade):
    a.append(int(input(("Digite os numeros da primeira lista "))))
for x in range(quantidade):
    b.append(int(input("Digite os numeros da segunda lista ")))
for y in range(quantidade):
    c.append(a[y]+b[y])
print(a)
print(b)
print(c)
