while True:
    try:
        v = float(input())
        d = float(input())
        h = 3.14 * ((d / 2) ** 2)
        a = v / h
        print(f'ALTURA = {a:.2f}')
        print(f'AREA = {h:.2f}')
    except EOFError:
        break