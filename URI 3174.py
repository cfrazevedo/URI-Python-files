n = int(input())
b = a = m = d = 0
for _ in range(n):
    e, g, h = input().split()
    if g == 'bonecos':
        b += int(h)
    elif g == 'arquitetos':
        a += int(h)
    elif g == 'musicos':
        m += int(h)
    elif g == 'desenhistas':
        d += int(h)
p = (b // 8) + (a // 4) + (m // 6) + (d // 12)
print(p)