g = 0
l = []
n = 0
while g != 3:
    cc = str(input())
    if cc == 'caw caw':
        g += 1
        l.append(n)
        n = 0
    else:
        for c, d in enumerate(cc):
            if d == '*':
                n += 2 ** ((len(cc) - 1) - c)
for c in l:
    print(c)