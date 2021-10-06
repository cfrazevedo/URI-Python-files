n = int(input())
for ne in range(n):
    t = int(input())
    p = [input() for _ in range(t)]
    u = int(input())
    r = []
    if ne != 0:
        print()
    for _ in range(u):
        perigo = False
        e = input()
        for c in p:
            if c in e:
                try:
                    if e[e.find(c) + len(c)].isalpha() and not e[e.find(c) + len(c)].islower():
                        perigo = True
                        break
                except:
                    perigo = True
                    break
        if perigo:
            r.append('Abortar')
        else:
            r.append('Prossiga')
    for o in r:
        print(o)