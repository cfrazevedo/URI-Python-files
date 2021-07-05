n = int(input())
cm = []
for c in range(0, n + 1):
    cm.append([int(x) for x in input().split()])
for c in range(0, n):
    for d in range(0, n):
        if cm[c][d] + cm[c + 1][d] + cm[c][d + 1] + cm[c + 1][d + 1] > 1:
            print('S', end='')
        else:
            print('U', end='')
    print()