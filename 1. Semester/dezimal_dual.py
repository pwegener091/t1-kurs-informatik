x = int(input("Dezimalzahl: "))

Reste = ""

while x > 0:
    Reste = str(x % 2) + Reste
    x = x // 2

print(Reste)
