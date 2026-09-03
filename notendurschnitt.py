noten = {"Anna": 1.3, "Ben": 2.7, "Clara": 1.0, "David": 3.3, "Elena": 1.7}

summe = 0
for x,y in noten.items():
    summe += y

#alternativ könnten wir folgendes benutzen.
#summe = (sum(noten.values()))

durchschnitt = summe / len(noten)
print(durchschnitt)

for x,y in noten.items():
    if y < durchschnitt:
        print(x)