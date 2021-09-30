a = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]
t = 0
for x in range(3):
    if r[x] > a[x]:
        t += r[x] - a[x]
print(t)