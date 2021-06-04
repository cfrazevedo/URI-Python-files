n = int(input())
t = []
lt = []
for c in range(0, n):
    l = 'D.C.'
    a = int(input())
    a = 2015 - a
    if a <= 0:
        a = abs(a) + 1
        l = 'A.C.'
    t.append(a)
    lt.append(l)
for c in range(0, n):
    print(f'{t[c]} {lt[c]}')