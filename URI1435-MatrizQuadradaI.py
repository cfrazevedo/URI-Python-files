x = int(input())
ms = []
m = []
while x != 0:
    if x % 2 == 0:
        c = x / 2
    else:
        c = (x + 1) / 2
    for linha in range(0, x):
        m.append([])
        for coluna in range(0, x):
            m[linha].append(1)
    valor = 1
    cima = 0
    esq = 0
    baixo = x - 1
    di = x - 1
    while valor <= c:
        for cont in range(esq, di + 1):
            m[cima][cont] = valor
            m[baixo][cont] = valor
        for cont in range(cima, baixo):
            m[cont][esq] = valor
            m[cont][di] = valor
        valor += 1
        cima += 1
        esq += 1
        baixo -= 1
        di -= 1
    ms.append(m[:])
    m.clear()
    x = int(input())
for b in ms:
    for d in b:
        for e, f in enumerate(d):
            if e == len(d) - 1:
                print('{:3}'.format(f))
            else:
                print('{:3}'.format(f), end=" ")
    print()