def f(n, liste=None):
    if liste is None:
        liste = []
    if n <= 0:
        return liste
    liste.append(n)
    return f(n - 2, liste)

print(f(6))