p = []
i = []
for e in range(0, 15):
    x = int(input())
    if x % 2 == 0:
        p.append(x)
    else:
        i.append(x)
    if len(i) == 5:
        for c, d in enumerate(i):
            print(f'impar[{c}] = {d}')
        i.clear()
    if len(p) == 5:
        for c, d in enumerate(p):
            print(f'par[{c}] = {d}')
        p.clear()
for c, d in enumerate(i):
    print(f'impar[{c}] = {d}')
for c, d in enumerate(p):
    print(f'par[{c}] = {d}')