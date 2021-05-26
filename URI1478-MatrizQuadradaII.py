ms = []
m = []
while True:
    x = int(input())
    if x == 0:
        break
    for linha in range(0, x):
        m.append([])
        for coluna in range(0, x):
            m[linha].append(1)
    n = 0
    while n <= x:
        valor = 0
        for cont in range(n, x):
            valor += 1
            m[n][cont] = valor
            m[cont][n] = valor
        n += 1
    ms.append(m[:])
    m.clear()
for b in ms:
    for d in b:
        for e, f in enumerate(d):
            if e == len(d) - 1:
                print('{:3}'.format(f))
            else:
                print('{:3}'.format(f), end=" ")
    print()