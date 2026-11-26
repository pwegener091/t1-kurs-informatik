def f(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return 1 + f(n - 2)
    else:
        return 1 + f(n - 1)

print(f(5))