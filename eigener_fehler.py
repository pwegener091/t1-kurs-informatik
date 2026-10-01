i = 0

def werfen():
    global i
    i += 1
    if i > 7:
        raise ValueError


while True:
    try:
        werfen()
        print(i)
    except ValueError:
        print("Ausnahme")
        break
    