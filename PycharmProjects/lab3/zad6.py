def iloczyn(a=1, b=4, ile=10):
    # il = a * (b**(ile-1))
    # return il
    elementy = []
    elementy.append(a)
    for x in range(0, ile-1):
        element = elementy[x]*b
        elementy.append(element)

    il = 1
    for x in range(0, ile):
        il = il * elementy[x]

    return elementy, il



print(iloczyn())
