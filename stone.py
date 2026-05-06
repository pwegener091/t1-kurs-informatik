a = int(input("Höhe: "))
b = int(input("Breite: "))

#for _ in range(a):
#    print("#"*b)

for _ in range(a):
    for _ in range(b):
        print("#", end = "")
    print()

