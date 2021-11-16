while True:
    x, m = [int(l) for l in input().split()]
    if x == 0 and m == 0:
        break
    print(x * m)