while True:
    try:
        hm = input()
        t = [float(x) for x in input().split()]
        media = sum(t) / len(t)
        ps = 0
        for test in t:
            ps += (test - media) ** 2
        ps = (ps/ (len(t) - 1)) ** (1 / 2)
        print(f'{ps:.5f}')
    except EOFError:
        break