x = 80

while x > 0:
    print(f"Es fehlen noch {x} Cents.")
    geld = int(input("Bitte Münze einwerfen: "))
    if geld in [5, 10, 20 ,50]:
        x = x - geld
    else:
        print("Keine gueltige Muenze")

print(f"Sie bekommen {abs(x)} Cents zurück.")