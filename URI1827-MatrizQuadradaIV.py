while True:
    try:
        x = int(input())
        m = []
        c = x // 2
        t = x // 3
        for linha in range(0, x):
            m.append([])
            for coluna in range(0, x):
                if linha == coluna == c:
                    m[linha].append(4)
                elif t <= linha <= x - t - 1 and t <= coluna <= x - t - 1:
                    m[linha].append(1)
                elif linha == x - coluna - 1:
                    m[linha].append(3)
                elif linha == coluna:
                    m[linha].append(2)
                else:
                    m[linha].append(0)
        for d in m:
            for e, f in enumerate(d):
                if e == len(d) - 1:
                    print(f)
                else:
                    print(f, end="")
        print()
    except EOFError:
        break