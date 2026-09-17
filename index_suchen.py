L = [11, 4, 34, 70, 80, 42]

#def index(L, x):
#    for i in range(len(L)):
#        if L[i] == x:
#            return i
#
#print(index(L, 70))

L = [11, 4, 34, 70, 80, 42]

def index_rekursiv(L, x, index=0):

    if L[index] == x:
        return index
    else:
        return index_rekursiv(L, x, index+1)    

print(index_rekursiv(L,42))
