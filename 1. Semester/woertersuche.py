wort = "abcodeejdkdcopedlcolekjkdkcore"
x = 0

for i in range(len(wort)-4+1):
    a = wort[i:i+4]
    if a[0:2] == "co" and a[3] == "e":
        x = x+1

print(x)