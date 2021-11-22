n = int(input())
r = 0
for _ in range(n):
    t, c = input().split()
    if t == 'G':
        r -= int(c)
    elif t == 'V':
        r += int(c)
if r < 0:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
else:
    print('A greve vai parar.')