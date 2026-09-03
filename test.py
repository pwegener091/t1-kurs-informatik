class Auto():

    def __init__(self, marke, farbe, ersterBesitzer, tueren = 4, plaetze = 4):
        self.tueren = tueren
        self.plaetze = plaetze
        self.marke = marke
        self.farbe = farbe
        self.besitzer = [ersterBesitzer] # Ein-Elementige Liste

    def wechsleBesitzer(self, neuerBesitzer):
        self.besitzer.append(neuerBesitzer)

    def aktuellerBesitzer(self):
        return self.besitzer[-1]
        
    def __str__(self):
        return f"Ein {str(self.farbe)}er {str(self.marke)}"


class Person():

    def __init__(self, name, alter, adresse):
        self.name = name
        self.alter = alter
        self.adresse = adresse
    def __repr__(self):
        return f"{self.name}, {self.alter} Jahre, aus {self.adresse}"

p1 = Person('Albert Einstein', 130, 'Princeton')
p2 = Person('Hannah Arendt', 110, 'New York')
a = Auto('Porsche', 'rot', p1, 3, 2)
a.wechsleBesitzer(p2)
print(a.aktuellerBesitzer())
print(a.besitzer)