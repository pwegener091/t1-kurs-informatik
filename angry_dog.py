def main():
    # get_number fragt den User nach einer positven Zahl
    # wuff gibt entsprechend oft "wuff" aus 
    wuff(get_number())  
    

# getnumber() soll den User solange fragen bis er eine positive Zahl eingibt
def get_number(): 
    fortsetzen = True
    while fortsetzen:
        n = int(input("Geben Sie eine Zahl ein: "))
        if n > 0:
            fortsetzen = False
    
    return n

# Funktion wuff(n) soll n mal "wuff" ausgeben
def wuff(n):
    for _ in range(n):
        print("wuff")


main()



