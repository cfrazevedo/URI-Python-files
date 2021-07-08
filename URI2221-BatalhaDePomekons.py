t = int(input())
r = []
for c in range(0, t):
    b = int(input())
    a1, d1, l1 = [int(x) for x in input().split()]
    a2, d2, l2 = [int(x) for x in input().split()]
    vg1 = (a1 + d1) / 2
    vg2 = (a2 + d2) / 2
    if l1 % 2 == 0:
        vg1 += b
    if l2 % 2 == 0:
        vg2 += b
    if vg1 == vg2:
        print('Empate')
    elif vg1 > vg2:
        print('Dabriel')
    else:
        print('Guarte')