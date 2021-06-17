n = int(input())
h = [int(x) for x in input().split()]
x = ''
for c in range(1, n):
    if h[c] == h[c - 1]:
        x += 'l'
    elif h[c] > h[c - 1]:
        x += 'p'
    elif h[c] < h[c - 1]:
        x += 'v'
if 'l' in x or 'pp' in x or 'vv' in x:
    print('0')
else:
    print('1')