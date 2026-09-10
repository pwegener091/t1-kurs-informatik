"""
Erstelle aus einer Zahlenreihe range(1, 11) ein Dictionary quadrat_gerade,
bei dem nur für gerade Zahlen das Quadrat der Zahl als Wert gespeichert wird (Schlüssel: Zahl,
Wert: Quadratzahl)
"""

quadrat_gerade = {k: k**2 for k in range(1,11) if k % 2 == 0}
print(quadrat_gerade)