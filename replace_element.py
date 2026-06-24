def replace_element(l, x, y):
    # jedes Mal, wenn x in l vorkommt, soll es durch y ersetzt werden
    i = 0
    while i < len(l):
        if l[i] == x:
            l[i] = y
            #l.insert(i,y)
            #l.remove(l[i+1])
        i += 1
    return l

print(replace_element([132, 40, 0, 1, 0, 100, 0], 0, "Nix"))



