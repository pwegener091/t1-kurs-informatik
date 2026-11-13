# wir wollen die Funktion konvertiere_datum testen

from datum import konnvertiere_datum

def main():
    test_normalfall()
    test_einstellig()
    test_fehler()
    test_fehler2()
    print("Alle Tests bestanden.")

def test_normalfall():
    assert konnvertiere_datum("11/12/2026") == "2026-11-12"
    assert konnvertiere_datum("10/31/2026") == "2026-10-31"

def test_einstellig():
    assert konnvertiere_datum("1/1/2026") == "2026-01-01"

def test_fehler():
    try:
        konnvertiere_datum("")
    except ValueError:
        pass
    else:
        assert False, "Bei leerer Eingabe fehlt der Value Error"

def test_fehler2():
    try:
        konnvertiere_datum("11/32/2026")
    except ValueError:
        pass
    else:
        assert False, "Angabe der Tage ist zu groß"

if __name__ == "__main__":
    main()