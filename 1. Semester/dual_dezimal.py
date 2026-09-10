x = input("Dualzahl: ")

# Dezimalzahl am Ende soll y sein
y = 0

for i in range(len(x)):
    y += int(x[i]) * (2**(len(x)-1-i))

print(y)