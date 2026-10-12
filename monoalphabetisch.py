ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def haeufigkeiten(text):
    zaehler = {}
    for zeichen in ALPHABET:
        zaehler[zeichen] = 0
    for zeichen in text.upper():
        if zeichen in ALPHABET:
            zaehler[zeichen] += 1

    return zaehler


def entschluesseln(geheimtext, zuordnung):
    ergebnis = ""
    for zeichen in geheimtext:
        if zeichen in zuordnung:
            ergebnis += zuordnung[zeichen].lower()
        else:
            ergebnis += zeichen
    return ergebnis

geheimtext = """KTQQHXDYRDY QOVA ADY QLGMPDQQDM SP PVQDYDW AOCORTMDV MDJDV ADQGTMJ QXMMRD WTV QOD
QXYCNTDMROC HTDGMDV DOV CPRDQ KTQQHXYR OQR MTVC PVA DVRGTDMR EDOVD HXDYRDY AOD OV
DOVDW HXDYRDYJPLG QRDGDV JDQXVADYQ QOLGDY QOVA MTVCD QTDRSD TPQ ADVDV WTV QOLG DOV
KTQQHXYR TJMDORDR ADVV AODQD ETVV WTV QOLG CPR WDYEDV PVA QOD QOVA RYXRSADW QLGHDY
SP DYYTRDV TPQQDYADW QXMMRD WTV NPDY BDADV AODVQR DOV DOCDVDQ KTQQHXYR IDYHDVADV"""


print(haeufigkeiten(geheimtext))
print(entschluesseln(geheimtext, {"I": "V", "N": "F", "E": "K", "L": "C", "S": "Z", "P": "U", "K": "P", "H": "W","G": "H", "J": "B", "W": "M", "X": "O", "T": "A", "M": "L", "D": "E", "R": "T", "C": "G", "B": "J", "O": "I", "V": "N", "Q": "S", "A": "D", "Y": "R"}))