teste = 0
while True:
    m = int(input())
    if m == 0:
        break
    teste += 1
    t = 0
    op = input()
    l = op.split('+')
    for c in l:
        try:
            n = int(c)
            t += n
            l.remove(c)
        except:
            continue
    for d in l:
        lm = d.split('-')
        t += int(lm[0])
        for e in range(1, len(lm)):
            t -= int(lm[e])
    print(f'Teste {teste}')
    print(t)
    print()