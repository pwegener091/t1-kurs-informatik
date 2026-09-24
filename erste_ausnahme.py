while True:
    try:
        n = int(input("Ganze Zahl eingeben: "))
        print(n/(n-4))
        break
    except ValueError:
        print("Das war keine Zahl")
        print("Bitte nochmal eingeben.")
    except ZeroDivisionError:
        print("Nicht durch 0 teilen!")
