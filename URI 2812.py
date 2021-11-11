n = int(input())
for c in range(0, n):
    m = int(input())
    mi = [int(x) for x in input().split()]
    mi.sort(reverse=True)
    imp = []
    while True:
        mud = False
        for d in mi:
            if d % 2 == 1:
                imp.append(d)
                mi.remove(d)
                mi.reverse()
                mud = True
                break
        if mud == False:
            break
    print(*imp)

