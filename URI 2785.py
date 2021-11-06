n = int(input())
m = [[int(x) for x in input().split()] for _ in range(n)]
p = [m[0]]
for c in range(1, n):
    i = 0
    j = i + c + 1
    p.append([])
    for d in range(n - c):
        e1 = p[c - 1][d]
        e2 = p[c - 1][d + 1]
        if e1 < e2:
            ee = e1
        else:
            ee = e2
        e = sum(m[c][i:j]) + ee
        p[c].append(e)
        i += 1
        j += 1
print(p[-1][-1])
