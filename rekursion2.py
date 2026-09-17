def f(n):
    if n <= 0:
        return 0
    else:
        return n + f(n-1)

eingabe = int(input("n: "))
print(f(eingabe))