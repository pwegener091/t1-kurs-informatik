#def fakultaet(n):
#    produkt = 1
#    for i in range(1,n+1):
#        produkt *= i
#    return produkt

def fakultaet(n):
    if n > 1:
        return n * fakultaet(n-1)
    elif n == 1:
        return 1

print((fakultaet(43)*fakultaet(6))/fakultaet(49))