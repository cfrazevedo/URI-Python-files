t = int(input())
magia = {
    'fire': (200, 20, 30, 50),
    'water': (300, 10, 25, 40),
    'earth': (400, 25, 55, 70),
    'air': (100, 18, 38, 60)
}

for c in range(t):
    w, h, xo, yo = [int(x) for x in input().split()]
    mag, *resto = input().split()
    n, cx, cy = [int(x) for x in resto]
    dist = 0
    dn = 0

    if cx < xo:
        if cy < yo:
            dist = (((cx - xo) ** 2) + ((cy - yo) ** 2)) ** (1/2)
        elif cy > yo + h:
            dist = (((cx - xo) ** 2) + ((cy - (yo + h)) ** 2)) ** (1/2)
        else:
            dist = xo - cx
    elif cx > xo + w:
        if cy < yo:
            dist = (((cx - (xo + w)) ** 2) + ((cy - yo) ** 2)) ** (1/2)
        elif cy > yo + h:
            dist = (((cx - (xo + w)) ** 2) + ((cy - (yo + h)) ** 2)) ** (1/2)
        else:
            dist = cx - (xo + w)
    else:
        if cy > yo + h:
            dist = cy - (yo + h)
        elif cy < yo:
            dist = yo - cy

    if dist <= magia[mag][n]:
        dn = magia[mag][0]

    print(dn)