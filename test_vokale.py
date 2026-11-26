def anzahl_vokale ( wort ):
    if wort == "":
        return 0
    elif len ( wort ) == 1:
        if wort in "aeiou" :
            return 1
        return 0

    rest = anzahl_vokale(wort[1:])

    if wort [0] in "aeiou" :
        return 1 + rest
    return rest

def test_anzahl_vokale():
    assert anzahl_vokale ( "haus" ) == 2
    assert anzahl_vokale ( "a" ) == 1
    assert anzahl_vokale ( "" ) == 0
    print ( " Alle Tests bestanden " )

test_anzahl_vokale()