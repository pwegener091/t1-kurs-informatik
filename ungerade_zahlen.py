liste = list(range(10001))

for i in liste:
    if i % 2 != 0:  # überprüfen ob dies eine ungerade Zahl ist
        liste.remove(i)

print(liste[:100])