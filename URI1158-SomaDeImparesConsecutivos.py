n = int(input())
ln = []
for c in range(0, n):
    l = input().split()
    x = int(l[0])
    y = int(l[1])
    s = 0
    for d in range(x, x + (2 * y)):
        if d % 2 == 1:
            s += d
    ln.append(s)
for c in ln:
    print(c)