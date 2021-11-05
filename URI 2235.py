l = [int(x) for x in input().split()]
l.sort()
if l[0] == l[1] or l[1] == l[2] or l[2] == l[1] + l[0]:
    print('S')
else:
    print('N')