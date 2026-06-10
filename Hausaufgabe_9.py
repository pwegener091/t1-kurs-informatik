produkte = [
"Laptop",
"Maus",
"Tastatur",
"FEHLER",
"Monitor",
"Maus",
"Tablet",
"ALT",
"Drucker",
"FEHLER",
"Scanner",
"Webcam",
"ALT",
"Lautsprecher",
"Mikrofon"
]

# (a) Einträge "FEHLER" durch "Unbekannt" ersetzen 
for i in range(len(produkte)):
    if produkte[i] == "FEHLER":
        produkte[i] = "Unbekannt"

# (b) Einträge "ALT" entfernen
produkte = [x for x in produkte if x != "ALT"]

#while "ALT" in produkte:
#    produkte.remove("ALT")

# (c) 
produkte.append("SSD")
produkte.append("Grafikkarte")

# (d)
for i in range(len(produkte)):
    if produkte[i] == "Webcam":
        produkte.insert(i, "Headset")
        break   

# (e)
produkte2 = []
for i in produkte:
    if i not in produkte2:
        produkte2.append(i)

produkte = produkte2

# (f) 
for x in range(len(produkte)):
    print(x+1, produkte[x])
