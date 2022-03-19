import random

lista = []
for i in range (1, 11):
    lista.append(random.randint(1, 100))

lista2 = [x for x in lista if x % 2 == 0]

print(lista2)