while True:
    try:
        d = []
        n = []
        t = int(input())
        for c in range(0, t):
            o = input().split()
            d.append(o)
        for c in range(0, t):
            j = input().split()
            nome = str(j[0])
            qo = int(j[1]) - 1
            to = str(j[2])
            oe = d[qo]
            oe1 = int(oe[0])
            oe2 = int(oe[1].split('=')[0])
            oef = int(oe[1].split('=')[1])
            if to == '+':
                if oe1 + oe2 != oef:
                    n.append(nome)
            if to == '-':
                if oe1 - oe2 != oef:
                    n.append(nome)
            if to == '*':
                if oe1 * oe2 != oef:
                    n.append(nome)
            if to == 'I':
                if oe1 + oe2 == oef or oe1 - oe2 == oef or oe1 * oe2 == oef:
                    n.append(nome)
        if len(n) == 0:
            print('You Shall All Pass!')
        elif len(n) == t:
            print('None Shall Pass!')
        else:
            nl = sorted(n)
            print(*nl)
    except EOFError:
        break