from math import ceil

v, n = [int(x) for x in input().split()]
p = (v * n) / 10
for _ in range(8):
    print(ceil(p), end=' ')
    p += (v * n) / 10
print(ceil(p))