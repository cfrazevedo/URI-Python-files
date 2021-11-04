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
        d1 = d2 = 0
        d1 += e1
        d2 += e2
        for i in range(n):
            d1 += a1[i]
            d2 += a2[i]
            if n != 1 and i != n - 1:
                if d1 + t1[i] < d2:
                    d2 = d1 + t1[i]
                elif d2 + t2[i] < d1:
                    d1 = d2 + t2[i]
        d1 += x1
        d2 += x2
        if d1 < d2:
            print(d1)
        else:
            print(d2)

    except EOFError:
        break
