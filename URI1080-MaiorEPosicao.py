m = p = 0
for c in range(1, 101):
    n = int(input())
    if n > m:
        m = n
        p = c
print(m)
print(p)