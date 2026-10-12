while True:
    eingabe = input("Bitte geben Sie ein Datum im Format MM/TT/JJJJ ein: ")

    try:
        monat_str, tag_str, jahr_str = eingabe.split("/")

        m = int(monat_str)
        t = int(tag_str)
        j = int(jahr_str)
        if 1 <= m <= 12 and 1 <= t <= 31 and 0 <= j<= 9999:
            print(f"{j:04d}-{m:02d}-{t:02d}")
            break
        else:
            print("Ungültige Zahlenwerte")


    except ValueError:
        print("Fehler: Bitte verwenden Sie das richtige Format")