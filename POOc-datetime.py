from datetime import datetime
dias=["segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domigo"]
x=datetime.datetime.now()
print(x.hour)
print(x.month)
print(x.year)
print(x.weekday())
print(f'Hoje é dia {x.day} de {x.month} de {x.year} e hoje é {dias[x.weekday()]}')
