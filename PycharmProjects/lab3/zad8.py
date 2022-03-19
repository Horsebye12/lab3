def zakupy(**lista):
    dlugosc = len(lista)

    suma = sum(lista.values())

    return dlugosc, suma


print(zakupy(Chleb=5, Mąka=3, Jajka=4))
