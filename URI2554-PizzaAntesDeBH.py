while True:
    try:
        n, d = [int(x) for x in input().split()]
        data = 'Pizza antes de FdI'
        evento = False
        for c in range(d):
            dia, *i = input().split()
            i = [int(x) for x in i]
            if evento:
                pass
            else:
                if not 0 in i:
                    evento = True
                    data = dia
        print(data)
    except EOFError:
        break