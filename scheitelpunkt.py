# Funktion, die die Scheitelpunktsform der Funktion
# f(x) = ax²+bx+c berechnet
def spf(a,b,c):
    # x-Wert des Scheitelpunkts
    xs = -b/(2*a)
    # y-Wert des Scheitelpunkts
    ys = (4*a*c-b**2)/(4*a)
    funktion = f"{a}(x-{xs})²+{ys}"
    funktion = funktion.replace("--","+")
    funktion = funktion.replace("+-","-")
    print(funktion)
    
spf(5,-3,7)