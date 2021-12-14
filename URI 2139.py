while True:
    try:
        ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        l = input().split()
        m = int(l[0])
        d = int(l[1])
        ms.append(d)
        x = 360
        for c in range(0, m - 1):
            x -= ms[c]
        x -= d
        if x < 0:
            print('Ja passou!')
        elif x == 0:
            print('E natal!')
        elif x == 1:
            print('E vespera de natal!')
        else:
            print(f'Faltam {x} dias para o natal!')
    except EOFError:
        break