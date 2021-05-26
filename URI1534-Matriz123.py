while True:
    try:
        x = int(input())
        m = []
        for linha in range(0, x):
            m.append([])
            for coluna in range(0, x):
                if linha == x - coluna - 1:
                    m[linha].append(2)
                elif linha == coluna:
                    m[linha].append(1)
                else:
                    m[linha].append(3)
        for d in m:
            for e, f in enumerate(d):
                if e == len(d) - 1:
                    print(f)
                else:
                    print(f, end="")
    except EOFError:
        break