while True:
    try:
        n = int(input())
        vr = 0
        r = []
        for c in range(n):
            t, d = [int(x) for x in input().split()]
            v = d / t
            if v > vr:
                vr = v
                r.append(c + 1)
        print(*r, sep="\n")
    except EOFError:
        break