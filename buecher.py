buecher = [
    {"Titel": "Der Hobbit", "Autor": "J.R.R. Tolkien", "Jahr": 1937, "Ausgeliehen": True},
    {"Titel": "Faust", "Autor": "Johann Wolfgang von Goethe", "Jahr": 1808, "Ausgeliehen": False},
    {"Titel": "Python Crashkurs", "Autor": "Eric Matthes", "Jahr": 2019, "Ausgeliehen": False},
    {"Titel": "Anonymes Werk", "Autor": None, "Jahr": 1500, "Ausgeliehen": False}
]

"""
Schreibe eine Funktion verfuegbare_buecher(buecher_liste), die alle Bücher ausgibt, die
nicht ausgeliehen sind. Falls der Autor None ist, soll stattdessen "Unbekannt" ausgegeben
werden
"""

def verfuegbare_buecher(buecher):
    for buch in buecher:
        if buch["Ausgeliehen"] == False:
            print(buch["Titel"])


verfuegbare_buecher(buecher)