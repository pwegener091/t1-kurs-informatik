wertepaare = [(1,1), (1,2), (1,3), (2,1), (2,2),(2,3)]

def f(x,y):
    return x**2 + y**2

for x,y in wertepaare: # man entpackt das Tupel
    print(x, y, f(x,y))