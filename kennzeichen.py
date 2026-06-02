def main():
    kennzeichen = input("Kennzeichen: ")
    if is_valid(kennzeichen):
        print("erlaubt")
    else:
        print("nicht erlaubt")


def is_valid(s):
    liste = s.split(" ")

    if len(liste) != 3:
        return False

    a = liste[0] # sollte MR oder GI sein
    b = liste[1] # 1-2 Buchstaben + Extrabedingungen
    c = liste[2] # 1-4 Ziffern, erste Ziffer nicht 0

    if a != "GI" and a != "MR":
        return False
    
    if b.isalpha():
        if b in ["KZ", "HJ", "NS", "SA", "SS"]:
            return False
        elif len(b) not in range(1,3):
            return False
        elif b != b.upper(): # ueberpruefen ob Großbuchstaben verwendet wurden
            return False
    else:
        return False
    
    if c.isdigit():
        if c in ["18", "88", "28", "1888"]:
            return False
        elif len(c) not in range(1,5):
            return False
        elif c[0] == "0":
            return False
        else:
            return True
    else:
        return False

main()