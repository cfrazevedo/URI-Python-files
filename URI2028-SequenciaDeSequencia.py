x = 0
while True:
    try:
        n = int(input())
        s = [0]
        x += 1
        for c in range(0, n + 1):
            for d in range(0, c):
                s.append(c)
        if len(s) == 1:
            print(f'Caso {x}: 1 numero')
        else:
            print(f'Caso {x}: {len(s)} numeros')
        for c, d in enumerate(s):
            if c == len(s) - 1:
                print(d)
            else:
                print(d, end=' ')
        print()
    except EOFError:
        break