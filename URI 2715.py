while True:
    try:
        n = int(input())
        x = [int(z) for z in input().split()]
        i = d = y = 0
        c = (n + i) // 2
        while True:
            y = abs(sum(x[c:]) - sum(x[:c]))
            r = sum(x[c:]) / sum(x[:c])
            if r > 1:
                i = c
            elif r < 1:
                n = c
            else:
                break
            c = (n + i) // 2
            if d == c:
                if y > abs(sum(x[c - 1:]) - sum(x[:c -1])):
                    y = abs(sum(x[c - 1:]) - sum(x[:c - 1]))
                elif y > abs(sum(x[c + 1:]) - sum(x[:c + 1])):
                    y = abs(sum(x[c + 1:]) - sum(x[:c + 1]))
                break
            d = c
        print(y)
    except EOFError:
        break