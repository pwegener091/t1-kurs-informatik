a = float(input("Zahl: "))
# d soll die Genauigkeit sein
d = float(input("Genauigkeit: "))

# Startwert
x_alt = (a+1)/2
aktuelle_genauigkeit = d+1
# Anzahl Iterationen
i = 0

while aktuelle_genauigkeit > d:
    x_neu = x_alt - ((x_alt ** 2 -a) / (2*x_alt) )
    aktuelle_genauigkeit = abs(x_neu - x_alt)
    x_alt = x_neu
    i = i+1

print(f"Die Wurzel von {a} ist näherungsweise {x_neu}")
print(f"Es wurden {i} Iterationen berechnet.")
