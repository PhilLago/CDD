#faça uma função que recebe uma lista como argumento e crie uma nova lista, somente com números únicos
#A=[1,2,2,3,4,4,5,3,6,7,6,8]
a=[1,2,2,3,4,4,5,3,6,7,6,8]
b=[]

for x in range(0, len(a)):
    if a[x] not in b:
        b.append(a[x])
print(b)


