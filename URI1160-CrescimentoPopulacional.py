n = int(input())
ln = []
for c in range(0, n):
    l = input().split()
    pa = int(l[0])
    pb = int(l[1])
    g1 = float(l[2])
    g2 = float(l[3])
    t = 0
    while pa <= pb and t <= 100:
        pa += pa * (g1 / 100)
        pb += pb * (g2 / 100)
        pa = int(pa)
        pb = int(pb)
        t += 1
    ln.append(t)
for c in ln:
    if c == 101:
        print('Mais de 1 seculo.')
    else:
        print(f'{c} anos.')