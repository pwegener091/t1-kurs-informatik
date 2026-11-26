def f(basis, exp):
    if exp == 0:
        return 1
    return basis * f(basis, exp - 1)

print(f(2, -3))