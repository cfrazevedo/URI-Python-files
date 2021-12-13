c = [2, 5, 10, 20, 50, 100]
c2 = []
for d in c:
    for e in c:
        f = d + e
        if f not in c2:
            c2.append(f)
while True:
    l = input().split()
    if int(l[0]) == int(l[1]) == 0:
        break
    t = int(l[1]) - int(l[0])
    if t in c2:
        print('possible')
    else:
        print('impossible')