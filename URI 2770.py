while True:
    l = []
    try:
        x, y, m = [int(x) for x in input().split()]
        for c in range(m):
            xi, yi = [int(x) for x in input().split()]
            if (xi <= x and yi <= y) or (xi <= y and yi <= x):
                l.append("Sim")
            else:
                l.append("Nao")
        print(*l, sep='\n')
    except EOFError:
        break