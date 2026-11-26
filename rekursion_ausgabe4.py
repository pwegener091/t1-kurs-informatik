def f(n):
    if n <= 1:
        return n
    return f(f(n - 1)) + f(n - 2)

print(f(5))