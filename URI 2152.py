c = int(input())
for d in range(0, c):
    p = input().split()
    hh = int(p[0])
    mm = int(p[1])
    if p[2] == '0':
        print(f'{hh:02d}:{mm:02d} - A porta fechou!')
    elif p[2] == '1':
        print(f'{hh:02d}:{mm:02d} - A porta abriu!')