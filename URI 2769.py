# Questão Não Resolvida
# Problema de Time Limit Error

while True:
    try:
        n = int(input())
        e1, e2 = [int(x) for x in input().split()]
        a1 = [int(x) for x in input().split()]
        a2 = [int(x) for x in input().split()]
        if n != 1:
            t1 = [int(x) for x in input().split()]
            t2 = [int(x) for x in input().split()]
        x1, x2 = [int(x) for x in input().split()]
        a1[0] += e1
        a2[0] += e2
        a1[len(a1) - 1] += x1
        a2[len(a2) - 1] += x2
        t = s = 0
        for c in range(2 ** n):
            p = f'{int(bin(s)[2:])}'.rjust(n, '0')
            tx = 0
            for d, e in enumerate(p):
                if e == '0':
                    tx += a1[d]
                elif e == '1':
                    tx += a2[d]
                if n != 1:
                    if d != 0:
                        if e != p[d - 1]:
                            if p[d - 1] == '0':
                                tx += t1[d - 1]
                            elif p[d - 1] == '1':
                                tx += t2[d - 1]
            if t == 0 or t > tx:
                t = tx
            s += 1
        print(t)
    except EOFError:
        break