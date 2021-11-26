while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        m = sum([int(x) for x in input().split()])
        print(f'{m} {m}')
    else:
        p = [int(x) for x in input().split()]
        m = []
        r = 0
        for c in range(n):
            r -= 1
            m.append(p[c] + p[r])
        print(f'{max(m)} {min(m)}')