# Não resolvido

while True:
    try:
        n, p = [int(x) for x in input().split()]
        pesos = [int(x) for x in input().split()]
        pesos.sort()
        j1 = int((n + 1) / 4)
        j3 = int(3 * (n + 1) / 4)
        print(j1, j3)
        q1 = pesos[j1 - 1] + ((((n + 1) / 4) - j1) * (pesos[j1] - pesos[j1]))
        q3 = pesos[j3 - 1] + (((3 * (n + 1) / 4) - j3) * (pesos[j3] - pesos[j3]))
        print(q1, q3)
        iqr = (q3 - q1) * 1.5
        print(iqr)
        v = 0
        for peso in pesos:
            if peso < q1 - iqr or peso > q3 + iqr:
                v += 1
        x = p * v
        print(x)
    except EOFError:
        break