plik = open("liczby.txt", "w")

for x in range (1, 101):
    if x % 4 == 0:
        plik.write(str(x))
        plik.write(" ")

