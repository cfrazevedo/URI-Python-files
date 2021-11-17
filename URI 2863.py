while True:
    try:
        t = int(input())
        r = 0
        for tt in range(t):
            ti = float(input())
            if tt == 0 or r > ti:
                r = ti
        print(r)
    except EOFError:
        break