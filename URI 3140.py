while True:
    try:
        l = input()
        if '<body>' in l:
            while True:
                p = input()
                if '</body>' in p:
                    break
                print(p)
    except EOFError:
        break