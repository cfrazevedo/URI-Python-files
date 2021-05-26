while True:
    try:
        l = int(input())
        v = input().split()
        m = 0
        for c in range(0, l):
            if int(v[c]) > m:
                m = int(v[c])
        if m >= 20:
            n = 3
        elif m >= 10:
            n = 2
        else:
            n = 1
        print(n)
    except EOFError:
        break