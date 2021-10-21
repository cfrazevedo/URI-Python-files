while True:
    try:
        n = int(input())
        m, l = [int(x) for x in input().split()]
        bm = []
        for c in range(m):
            bm.append([int(x) for x in input().split()])
        bl = []
        for c in range(l):
            bl.append([int(x) for x in input().split()])
        cm, cl = [int(x) for x in input().split()]
        a = int(input())
        if bm[cm - 1][a - 1] == bl[cl - 1][a - 1]:
            print('Empate')
        elif bm[cm - 1][a - 1] > bl[cl - 1][a - 1]:
            print('Marcos')
        elif bm[cm - 1][a - 1] < bl[cl - 1][a - 1]:
            print('Leonardo')
    except EOFError:
        break