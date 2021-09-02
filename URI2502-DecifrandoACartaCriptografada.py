while True:
    try:
        e = input().split()
        c = int(e[0])
        n = int(e[1])
        c1 = str(input()).lower()
        c2 = str(input()).lower()
        for d in range(0, n):
            l = str(input())
            l = list(l)
            for f in range(0, c):
                x = c1[f]
                y = c2[f]
                x1 = x.upper()
                y1 = y.upper()
                for g in range(0, len(l)):
                    if l[g] == x:
                        l[g] = y
                    elif l[g] == y:
                        l[g] = x
                    elif l[g] == x1 and not l[g].isnumeric():
                        l[g] = y1
                    elif l[g] == y1 and not l[g].isnumeric():
                        l[g] = x1
            l = ''.join(l)
            print(l)
        print()
    except EOFError:
        break