while True:
    try:
        n, m = [int(x) for x in input().split()]
        l = []
        t = []
        for c in range(n):
            l.append([int(x) for x in input().split()])
        for i in range(n):
            ij = []
            for j in range(m):
                p = 0
                if l[i][j] == 1:
                    p = 9
                elif l[i][j] == 0:
                    if l[i - 1][j] == 1:
                        if i - 1 >= 0:
                            p += 1
                    try:
                        if l[i + 1][j] == 1:
                            p += 1
                    except:
                        pass
                    if l[i][j - 1] == 1:
                        if j - 1 >= 0:
                            p += 1
                    try:
                        if l[i][j + 1] == 1:
                            p += 1
                    except:
                        pass
                ij.append(p)
            t.append((ij[:]))
        for d in t:
            print(*d, sep='')
    except EOFError:
        break