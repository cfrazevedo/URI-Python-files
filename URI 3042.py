while True:
    p = 1
    pp = 0
    m = int(input())
    if m == 0:
        break
    for _ in range(m):
        s = [int(x) for x in input().split()]
        while s[p] == 1:
            if p == 0:
                p += 1
                pp += 1
            elif p == 2:
                p -= 1
                pp += 1
            elif p == 1:
                if s[0] == 0:
                    p -= 1
                else:
                    p += 1
                pp += 1
    print(pp)