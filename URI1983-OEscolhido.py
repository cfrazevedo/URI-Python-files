n = int(input())
m = 'Minimum note not reached'
nt = 0
for c in range(0, n):
    l = input().split()
    if float(l[1]) > nt:
        nt = float(l[1])
        if nt >= 8:
            m = l[0]
print(m)