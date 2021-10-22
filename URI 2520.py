while True:
    try:
        n, m = [int(x) for x in input().split()]
        cid = []
        c1 = c2 = l1 = l2 = 0
        for c in range(n):
            cid.append([int(x) for x in input().split()])
            for d in range(m):
                if cid[c][d] == 1:
                    l1 = c
                    c1 = d
                elif cid[c][d] == 2:
                    l2 = c
                    c2 = d
        print((abs(l1 - l2)) + (abs(c1 - c2)))
    except EOFError:
        break