ms = []
m = []
while True:
    x = int(input())
    if x == 0:
        break
    for linha in range(0, x):
        m.append([])
        for coluna in range(0, x):
            m[linha].append(2 ** (linha + coluna))
    ms.append(m[:])
    m.clear()
for b in ms:
    t = len(str(b[(len(b) - 1)][(len(b) - 1)]))
    for d in b:
        for e, f in enumerate(d):
            while len(str(f)) < t:
                f = ' ' + str(f)
            if e == len(d) - 1:
                print(f)
            else:
                print(f, end=" ")
    print()