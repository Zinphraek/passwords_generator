def rog_(n: int) -> list[str]:
    n_l = list()
    for i in range(1, n+1):
        a_var = bin(i).replace('0b', '')
        n_l.append(a_var)
    return n_l


print(rog_(2))
