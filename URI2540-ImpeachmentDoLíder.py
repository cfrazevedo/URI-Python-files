while True:
    try:
        n = int(input())
        v = input().split()
        nv = 0
        for c in range(n):
            if v[c] == '1':
                nv += 1
        if nv >= n * (2 / 3):
            print('impeachment')
        else:
            print('acusacao arquivada')
    except:
        break