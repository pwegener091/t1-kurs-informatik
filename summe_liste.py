zahlen = [1,2,[23, 44,[1,[2,[3]]],[5, [6,77]],82],99]

def aufsummieren(zahlen):
    summe = 0
    for wert in zahlen:
        if isinstance(wert, list):
            summe += aufsummieren(wert)
        else:
            summe += wert
    return summe

print(aufsummieren(zahlen))
print(aufsummieren([]))

