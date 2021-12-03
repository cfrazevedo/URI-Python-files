while True:
    k, l = map(int, input().split())
    if k == l == 0:
        break
    m = l
    for c in range(2, l):
        if k % c == 0:
            m = c
            print(f'BAD {m}')
            break
    if m == l:
        print('GOOD')
