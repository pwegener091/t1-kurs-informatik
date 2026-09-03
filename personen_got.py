personen = {
    "Arya": "Stark",
    "Cersei": "Lannister",
    "Daenerys": "Targaryen",
    "Jaime": "Lannister",
    "Jon": "Stark"
}


personen["Jon"] = "Targaryen" # Update
personen.update({"Jon": "Stark", "Tywin": "Lannister"})
personen["Tyrion"] = "Lannister" # neuer Eintrag
del personen["Arya"] # löschen eines Eintrags

#print(personen)

#for p in personen:
#    if personen[p] == "Lannister":
#        print(f"{p} {personen[p]}")

#for x,y in personen.items():
#    if y == "Lannister":
#        print(f"{x} {y}")

Lannisters = [vorname for vorname in personen if personen[vorname] == "Lannister"]
print(Lannisters)