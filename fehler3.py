while True:
    n = input("Bitte eine Zahl eingeben: ")
    if n.isnumeric():
        print(float(n) * 4)
        break   
    else:
        print("Bitte eine Zahl eingeben!")