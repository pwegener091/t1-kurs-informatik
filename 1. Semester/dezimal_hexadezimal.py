print("Umrechnung von Dezimal- in Hexadezimalzahl")
x = int(input("Dezimalzahl: "))

Reste = ""
# legen ein dictionary an; mehr dazu im nächsten Semester
zahlen = {10: "a",11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}


while x > 0:
    Rest = x % 16
    if Rest < 10:
        Reste = str(x % 16) + Reste
    else:
        Reste = zahlen[Rest] + Reste
    x = x // 16

print(f"Hexadezimalzahl: {Reste}")