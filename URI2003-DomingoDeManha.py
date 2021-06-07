while True:
    try:
        h = input().split(':')
        m = 0
        if int(h[0]) >= 7:
            m = ((int(h[0]) - 7) * 60) + int(h[1])
        print(f'Atraso maximo: {m}')
    except EOFError:
        break