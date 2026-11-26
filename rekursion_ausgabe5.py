def f(n, k=1):
    if n <= 0:
        return 0
    if k % 2 == 1:
        return n + f(n - 1, k + 1)
    else:
        return f(n - 1, k + 1)

print(f(5))