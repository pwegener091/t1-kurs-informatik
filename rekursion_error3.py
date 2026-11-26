def f(n):
    if n == 0:
        return 1
    return f(n - 1) + f(n - 1)

print(f(30))