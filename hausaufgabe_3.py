def generate_email(vorname, nachname, firma):
    vorname = vorname.lower()
    nachname = nachname.lower()
    print(f"{vorname}.{nachname}@{firma.lower()}.de")


def clean_text(satz, wort):
    satz = satz.replace(wort, "*"*len(wort))
    print(satz)

#clean_text("Alle Studierenden lieben das Fach Informatik", "Informatik")

def get_initials(name):
    # in name.split() werden zwei Werte berechnet: Vorname und Nachname
    vorname, nachname = name.title().split()
    print(f"{vorname[0]}.{nachname[0]}.")

#get_initials("anna lange")

def get_year(code):
    return code[5:9]

jahr = get_year("2371-2018-Cons")
print(jahr)

