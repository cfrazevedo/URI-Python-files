while True:
    try:
        nq = [int(x) for x in input().split()]
        ln = []
        for c in range(nq[0]):
            ln.append(int(input()))
        ln.sort(reverse=True)
        for c in range(nq[1]):
            p = int(input()) - 1
            print(ln[p])
    except EOFError:
        break