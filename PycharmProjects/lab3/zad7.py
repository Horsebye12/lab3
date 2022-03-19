def iloczyn(*liczby):

    elementy = []
    elementy.append(liczby[0])
    for x in range(0, liczby[2]-1):
        element = elementy[x]*liczby[1]
        elementy.append(element)

    il = 1
    for x in range(0, liczby[2]):
        il = il * elementy[x]

    return elementy, il


print(iloczyn(1, 2, 4))
