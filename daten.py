ergebnisse = [
("Alice", "Mathematik", 1.7),
("Bob", "Informatik", 2.3),
("Alice", "Informatik", 1.0),
("Charlie", "Mathematik", 3.0),
("Bob", "Mathematik", 2.0),
("Alice", "Physik", 1.3),
("Charlie", "Informatik", 2.7)
]

"""
Schreibe eine Funktion restrukturiere_daten(ergebnisse), die diese Daten in ein ver-
schachteltes Dictionary umwandelt. Der äußere Schlüssel soll der Schülername sein. Der innere
Wert soll wieder ein Dictionary sein, welches das Fach als Schlüssel und die Note als Wert
enthält.
Erstelle anschließend mithilfe von Dictionary Comprehension ein Dictionary durchschnitte,
welches jedem Schüler seinen Notendurchschnitt zuordnet.
"""

def restrukturiere_daten(ergebnisse):
    schueler = {}
    # schueler = {"Alice": {"Mathematik": 1.7, "Informatik": 1.0 ,..} "Bob": {...}, ...}
    for name, fach, note in ergebnisse:
        if name not in schueler:
            schueler[name] = {}  #2. durchlauf: schueler = {"Alice": {"Mathematik": 1.7}, "Bob": {}}
        schueler[name][fach] = note #2. durchlauf: schueler = {"Alice": {"Mathematik": 1.7}, "Bob": {"Inforamtik": 2.3}}
        
    return schueler

ergebnisse_neu = restrukturiere_daten(ergebnisse)
#print(ergebnisse_neu)

durchschnitte ={}
for x, y in ergebnisse_neu.items():
    summe = 0
    for fach in y:
        summe += y[fach]

    durchschnitt = round(summe/len(y), 2)
    durchschnitte[x] = durchschnitt

print(durchschnitte)



