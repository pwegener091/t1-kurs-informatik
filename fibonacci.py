ZAEHLER = 0

def fibonacci(n):
    global ZAEHLER # hiermit kann die Variable in der Funktion geändert werden
    ZAEHLER += 1
    if n <= 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


eingabe = int(input("n: "))
print(f"die {eingabe}-te Fibonacci-Zahl ist {fibonacci(eingabe)}")
print(f"Die Funktion fibonacci wurde {ZAEHLER} mal aufgerufen.")
