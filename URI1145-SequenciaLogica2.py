a = input().split()
x = int(a[0])
y = int(a[1])
for c in range (1, y + 1):
    print(c, end='')
    if c % x == 0:
        print()
    else:
        print(end=' ')