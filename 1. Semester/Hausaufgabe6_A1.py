a = input().split(",")
f = 0
total_sum = 0

while f != len(a):
    num = int(a[f])
    if num > 0:
        total_sum = num + total_sum
    f =f+1
print (total_sum)
