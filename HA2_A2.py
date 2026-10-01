def berechne_kassenbon(artikel_preise):
    gesamtsumme = 0
    for preis in artikel_preise:
        if preis >= 30:
            preis = preis * 0.80
            
        gesamtsumme = gesamtsumme + preis
        
    return f"Bitte zahlen Sie: {gesamtsumme} Euro."

# Test-Warenkorb
# (Erwartetes Ergebnis: 12.50 + 32.00 (Rabatt!) + 15.00 + 40.00 (Rabatt!) = 99.50 Euro)
#warenkorb = [12.50, 40.00, 15.00, 50.00]
warenkorb2 = [30, 30, 30]
print(berechne_kassenbon(warenkorb2))