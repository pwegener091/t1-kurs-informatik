budget = 50
preis = -1

while budget > 0 and preis != 0:
    print(f"Sie haben noch {budget:.2f} Euro übrig")
    preis = float(input("Was ist der Preis: "))
    if preis < 0:
        print("Ungueltiger Preis!") #Ungültiger Preis
    elif preis > budget:
        print("Das ist zu teuer!")
        #print(f"Sie haben nur noch {budget:.2f} Euro.")
    else: 
        budget = budget - preis

print(f"Sie haben noch {budget:.2f} Euro übrig.")
