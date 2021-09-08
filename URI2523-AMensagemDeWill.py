while True:
    try:
        abc = input()
        n = int(input())
        l = [int(x) for x in input().split()]
        f = ''
        for c in range(0, n):
            f += abc[l[c] - 1]
        print(f)
    except EOFError:
        break