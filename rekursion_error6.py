def f(liste):
    if len(liste) == 0:
        return []
    return [liste[-1]] + f(liste)

print(f([1, 2, 3]))