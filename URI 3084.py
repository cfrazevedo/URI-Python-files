while True:
    try:
        h, m = [int(x) for x in input().split()]
        hh = h // 30
        mm = m // 6
        print(f'{hh:02}:{mm:02}')
    except EOFError:
        break