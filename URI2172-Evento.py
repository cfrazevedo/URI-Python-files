while True:
    l = input().split()
    x = int(l[0])
    m = int(l[1])
    if x == 0 and m == 0:
        break
    print(x * m)