n = int(input())
l = []
for c in range(1, n + 1):
    l.append(int(input()))
for c in l:
    if c == 0:
        print('NULL')
    else:
        if c % 2 == 1:
            print('ODD', end=' ')
        elif c % 2 == 0:
            print('EVEN', end=' ')
        if c > 0:
            print('POSITIVE')
        elif c < 0:
            print('NEGATIVE')