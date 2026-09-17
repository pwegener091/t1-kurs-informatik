ZAEHLER = 0
FIB = {1: 1, 2: 1}

def fibonacci(n):
    global ZAEHLER, FIB # hiermit kann die Variable in der Funktion geändert werden
    ZAEHLER += 1
    if n in FIB:
        return FIB[n]
    else:
        f = fibonacci(n-1) + fibonacci(n-2)
        FIB[n] = f
        return f

eingabe = int(input("n: "))
print(f"die {eingabe}-te Fibonacci-Zahl ist {fibonacci(eingabe)}")
print(f"Die Funktion fibonacci wurde {ZAEHLER} mal aufgerufen.")