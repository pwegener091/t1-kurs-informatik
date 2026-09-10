# a ist globale Variable
a = 10

def mal_drei(x):
    x *= 3
    print(x)

mal_drei(a) # hier rechnet Python mit einer Kopie a 
print(a)