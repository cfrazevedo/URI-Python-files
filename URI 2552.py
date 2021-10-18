while True:
    try:
        n, m = [int(x) for x in input().split()]
        l = [[int(x) for x in input().split()] for c in range(n)]
        for i in range(n):
            ij = []
            for j in range(m):
                p = 0
                if l[i][j] == 1:
                    p = 9
                else:
                    if i - 1 >= 0 and l[i - 1][j] == 1:
                        p += 1
                    if i + 1 < n and l[i + 1][j] == 1:
                        p += 1
                    if j - 1 >= 0 and l[i][j - 1] == 1:
                        p += 1
                    if j + 1 < m and l[i][j + 1] == 1:
                        p += 1
                ij.append(p)
            print(*ij, sep='')
    except EOFError:
        break