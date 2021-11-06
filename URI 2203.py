while True:
    try:
        l = [int(x) for x in input().split()]
        d = ((((l[0] - l[2]) ** 2) + ((l[1] - l[3]) ** 2)) ** (1 / 2)) + (l[4] * 1.5)
        t = l[5] + l[6]
        if t >= d:
            print('Y')
        else:
            print('N')
    except EOFError:
        break