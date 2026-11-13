def main():
    Namen = input("Name: ")
    hallo(Namen) 
    tschuess(Namen)

def hallo(Namen):
    print(f"Hallo {Namen}")

def tschuess(Namen):
    print(f"Auf Wiedersehen {Namen}")

if __name__ == "__main__":
    main()

