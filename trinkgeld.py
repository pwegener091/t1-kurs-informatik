def main():
    euros = euros_to_float(input("Wie teuer war das Essen? "))
    prozent = prozent_to_float(input("Wie viel Prozent Trinkgeld wollen Sie geben? "))
    trinkgeld = euros * prozent
    print(f"Gib {trinkgeld:.2f} Euro Trinkgeld")

def euros_to_float(d): # d soll z.B. "123,35€"
    d = d.replace("€","") # d ist "123,35"
    d = d.replace(",",".") # d ist "123.35"
    return float(d) # es wird die float 123.25 zurückgegeben

def prozent_to_float(p): # p soll z.B. "12%" sein
    p = p.replace("%","")
    p = float(p) / 100
    return p

main()