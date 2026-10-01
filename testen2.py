def berechne_durchschnitt(zahlen):

    summe = 0
    for zahl in zahlen:
        summe += zahl

    if zahlen == []:
        return 0

    durchschnitt = (summe / len(zahlen))

    return durchschnitt

def test_durchschnitt():
    assert berechne_durchschnitt([10,20,30]) == 20.0, f"Ergebnis: {berechne_durchschnitt([10,20,30])}, erwartet: 20.0"
    assert berechne_durchschnitt([5]) == 5.0
    assert berechne_durchschnitt([-2,2]) == 0.0
    try:
        berechne_durchschnitt([])
    except ZeroDivisionError:
        pass
    else:
        assert False, "Kein ZeroDivisionError"
    print("alle Tests bestanden.")

test_durchschnitt()

