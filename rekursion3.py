
L = [1,2,[3,4,[5,6]],7]
M = []

def liste_glaetten(L):
    for x in L:
        if isinstance(x, int):
            M.append(x)
        elif isinstance(x, list):  
            liste_glaetten(x)
    return M


print(liste_glaetten(L))
