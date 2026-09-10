# Aufgabe 2
def sum_mod(x,y):
    return (x+y)%2


# Aufgabe 3
def lauter():
    satz = input("Eingabe: ")
    print(satz.upper())

def willkommen(nachname, vorname):
    print(f"Sehr geehrte(r) {vorname} {nachname},\n\n"\
          "herzlich Willkommen am Studienkolleg Mittelhessen!")
    
willkommen("Meier", "Michaela")