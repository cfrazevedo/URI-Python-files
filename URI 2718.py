n = int(input())
for _ in range(n):
    x = bin(int(input()))[2:]
    s = q = 0
    for c in x:
        if c == '1':
            q += 1
            if q > s:
                s = q
        if c == '0':
            q = 0
    print(s)