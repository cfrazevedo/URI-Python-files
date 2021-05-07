l3 = []
while True:
    l1 = input().split()
    a = int(l1[0])
    b = int(l1[1])
    l2 = []
    if a <= 0 or b <= 0:
        break
    else:
        if a <= b:
            m = a
            n = b + 1
        else:
            m = b
            n = a + 1
        for c in range(m, n):
            l2.append(c)
        l3.append(l2[:])
for c in range(0, len(l3)):
    for d in l3[c]:
        print(d, end=' ')
    print(f'Sum={sum(l3[c])}')