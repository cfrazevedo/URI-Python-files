while True:
    try:
        m = int(input())
        nc = c = 0
        for e in range(m):
            d = [int(x) for x in input().split()]
            nc += d[0] * d [1]
            c += d[1]
        print(f'{(nc / (c * 100)):.4f}')
    except EOFError:
        break