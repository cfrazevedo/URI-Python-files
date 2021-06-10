while True:
    t = int(input())
    p = []
    if t == 0:
        break
    for c in range(0, t):
        n = int(input())
        if n % 2 == 0:
            p.append((n * 2) - 2)
        else:
            p.append((n * 2) - 1)
    for c in p:
        print(c)