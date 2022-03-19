import math

print("Python comprehesion \n \n")

a = [x**2 for x in range(10)]
b = [3**i for i in range(6)]
c = [x for x in a if x % 2 == 1]

print("Przykład 1: ", a)
print(b)
print(c)

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [i for i in liczby if i % 2 == 0]

print("Przykład 2: ", lista2)

lista3 = [(i, j) for i in [1, 2, 3] for j in [4, 5, 6]]
print("Przykład 3: ", lista3)

skroty = {"PZU": "Państwowy zakład ubezpieczeń", "ZUS": "Zakład ubezpieczeń społecznych", "PKO": "Państwowa kasa oszczędności"}
odwrocone = {value: key for key, value in skroty.items()}
print("Przykład 4: ", odwrocone)

print("Funkcje \n \n")


def row_kwadratowe(q, w, e):
    delta = w**2 - 4 * q * e
    if delta < 0:
        print("Brak pierwiastków")
        return -1
    elif delta == 0:
        print("Jeden pierwiastek")
        x = (-w) / (2 * q)
        return x
    else:
        print("Dwa pierwsiastki")
        x1 = (-w - math.sqrt(delta)) / (2 * q)
        x2 = (-w + math.sqrt(delta)) / (2 * q)
        return x1, x2

print(row_kwadratowe(6, 1, 3))
print(row_kwadratowe(1, 2, 1))
print(row_kwadratowe(1, 4, 1))

def dlugosc_odcinka(x3 = 0, y3 = 0, x4 = 0, y4 = 0):
    return math.sqrt((x4 - x3) ** 2 + (y4 - y1) ** 2)


