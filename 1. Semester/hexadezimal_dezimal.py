print("Hexadezimalzahl in Dezimalzahl umrechnen")
x = input("Hexadezimalzahl: ")

# Dezimalzahl am Ende soll y sein
y = 0

werte = {"a": "10", "b": "11", "c": "12", "d": "13", "e": "14", "f": "15"}
for i in range(len(x)):
    zahl = x[i]
    if zahl in ["a", "b", "c", "d", "e", "f"]:
        y += int(werte[zahl]) * (16**(len(x)-1-i))
    else:
        y += int(zahl) * (16**(len(x)-1-i))

print(f"Dezimalzahl: {y}")