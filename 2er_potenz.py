zahl = str(2 ** 10000)

gesuchte_zahl = 5
# die lsite verbotene_zahlen enthaelt intergers und keine strings
verbotene_zahlen = list(range(10))
verbotene_zahlen.remove(gesuchte_zahl)


for i in verbotene_zahlen:
    zahl = zahl.replace(str(i), "0")

zahl = zahl.split("0")
#print(zahl)

max = 0 
# zahl ist jetzt eine Liste
for z in zahl:
    if len(z) > max:
        max = len(z)

print(max)


