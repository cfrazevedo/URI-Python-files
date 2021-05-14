n = 1
ln = []
while True:
    n = int(input())
    if n == 0:
        break
    s = 0
    for c in range(n, n + 10):
        if c % 2 == 0:
            s += c
    ln.append(s)
for c in ln:
    print(c)