x = 1
le = []
while x != 0:
    li = []
    x = int(input())
    for c in range(1, x + 1):
        li.append(c)
    le.append(li[:])
for c in le:
    for d in c:
        print(d, end='')
        if d == len(c):
            print()
        else:
            print(end=' ')