while True:
    try:
        n, i = [int(x) for x in input().split()]
        cont = 0
        for c in range(n):
            ii, j = [int(x) for x in input().split()]
            if i == ii and j == 0:
                cont += 1
        print(cont)
    except EOFError:
        break