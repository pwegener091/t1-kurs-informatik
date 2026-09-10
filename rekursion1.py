def f(x):
    if x > 1:
        print(x)
        f(x/2)

f(100)