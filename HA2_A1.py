def potenz(basis, exponent): #basis und exponent sind ganze Zahlen >=0
    if exponent == 0:
        return 1
    else: 
        return basis * potenz(basis, exponent-1)

print(potenz(9,2)) 

