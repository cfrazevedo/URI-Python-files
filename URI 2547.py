while True:
    try:
        n, p, g = [int(x) for x in input().split()]
        i = 0
        for c in range(n):
            a = int(input())
            if p <= a <= g:
                i += 1
        print(i)
    except EOFError:
        break