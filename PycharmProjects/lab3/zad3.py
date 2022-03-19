produkty = {"Mleko": "litry", "Ziemniaki": "kilogramy", "Chipsy": "sztuki", "Jajka": "sztuki"}

lista = []

for key, value in produkty.items():
    if (value == "sztuki"):
        lista.append("{key}".format(key=key))

print(lista)