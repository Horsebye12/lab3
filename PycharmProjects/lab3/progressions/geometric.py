def geo_item(a1, q, n):
    an = a1 * (q ** (n - 1))
    return an


def geo_sum(a1, q, n):
    if q == 1:
        sn = a1 * n
        return sn
    else:
        sn = a1 * ((1 - (q ** n)) / (1 - q))
        return sn
