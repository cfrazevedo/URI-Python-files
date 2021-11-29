from math import inf

n = int(input())
cn = []
f = []
for _ in range(n):
    cn.append([int(x) for x in input().split()])
for c in cn:
    on = cn[:]
    on.remove(c)
    dm = inf
    for ci in on:
        d = (((c[0] - ci[0]) ** 2) + ((c[1] - ci[1]) ** 2) + ((c[2] - ci[2]) ** 2)) ** (1 / 2)
        if d < dm:
            dm = d
    if dm <= 20:
        f.append('A')
    elif 20 < dm <= 50:
        f.append('M')
    elif dm > 50:
        f.append('B')
print(*f, sep='\n')