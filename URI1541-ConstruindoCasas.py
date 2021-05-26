while True:
    e = input().split()
    if '0' in e:
        break
    else:
        a = int(e[0])
        b = int(e[1])
        c = int(e[2])
    t = ((a * b) * 100) / c
    l = int(t ** (1 / 2))
    print(l)