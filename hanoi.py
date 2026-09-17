def hanoi(n, quelle, ziel, hilfe):
    if n == 1:
        print(f"Ziehe Scheibe von {quelle} zu {ziel}.")
    else:
        hanoi(n-1, quelle, hilfe, ziel)
        print(f"Ziehe Scheibe von {quelle} zu {ziel}.")
        hanoi(n-1, hilfe, ziel, quelle)

hanoi(3, "A", "C", "B")