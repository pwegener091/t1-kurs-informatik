mensa_gerichte = [
    "Spaghetti Bolognese", # Index 0 (Tag 1)
    "Veganes Curry",       # Index 1 (Tag 2)
    "Schnitzel mit Pommes",# Index 2 (Tag 3)
    "Milchreis",           # Index 3 (Tag 4)
    "Fischstäbchen"        # Index 4 (Tag 5)
]
try:
    tag = int(input("Gib den Tag als Zahl ein (1-5): "))

    # Da Listen bei 0 anfangen, ziehen wir 1 ab
    index = tag - 1
    gericht = mensa_gerichte[index]
except IndexError:
    print("Diesen Tag gibt es nicht auf dem Speiseplan")
except ValueError:
    print("Bitte eine Zahl eingeben")
else:
    print("Heute gibt es:", gericht)
finally:
    print("Ende.")

