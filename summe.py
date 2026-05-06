eingabe = input("Zahl: ")
summe = 0 

while eingabe != "":
    eingabe = float(eingabe)
    summe = summe + eingabe
    eingabe = input("Zahl: ")

print(f"Die Summe der Zahlen ist {summe}.")