def repeat_element(l, x, k):
    # in der Liste l soll der Eintrag x (wenn er vorkommt) um das k-fache 
    # vervielfacht werden
    i = 0
    while i < len(l):
        if l[i] == x:
            for j in range(k-1):
                l.insert(i+j, x)
            i += k
        else:
            i += 1

    return l


print(repeat_element(["a", "x", "y", "u", "x"], "x", 5))