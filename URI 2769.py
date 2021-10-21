# Questão Não Resolvida
# Problema de Memory Limit Error

from itertools import product

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
        p = [1, 2]
        pl = list(product(p, repeat=n))
        t = 0
        for c in pl:
            tx = 0
            for d, e in enumerate(c):
                if e == 1:
                    tx += a1[d]
                elif e == 2:
                    tx += a2[d]
                if n != 0:
                    if d != 0:
                        if e != c[d - 1]:
                            if c[d - 1] == 1:
                                tx += t1[d - 1]
                            elif c[d - 1] == 2:
                                tx += t2[d - 1]
            if t == 0 or t > tx:
                t = tx
        print(t)
    except EOFError:
        break