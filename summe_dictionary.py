ausgaben = {
    "Personal": 15000,
    "Marketing": {
        "Social Media": 1200,
        "Printmedien": 800
        },
    "Forschung_und_Entwicklung": {
        "Software": {
            "Lizenzen": 3500,
            "Cloud-Server": 2100
            },
        "Hardware": 4000
        },
    "Vertrieb": 5000
}

def aufsummieren(ausgaben):
    summe = 0
    for abteilung in ausgaben:
        if isinstance(ausgaben[abteilung], dict):
            summe += aufsummieren(ausgaben[abteilung])
        else:
            summe += ausgaben[abteilung]
    return summe

print(aufsummieren(ausgaben))
print(aufsummieren([1, 12]))