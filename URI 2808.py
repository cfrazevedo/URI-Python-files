l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
p1, p2 = input().split()
pos = []
if l.index(p1[0]) != 0:
    pos.append(f'{l[l.index(p1[0]) - 1]}{int(p1[1]) - 2}')
    pos.append(f'{l[l.index(p1[0]) - 1]}{int(p1[1]) + 2}')
if l.index(p1[0]) != 7:
    pos.append(f'{l[l.index(p1[0]) + 1]}{int(p1[1]) - 2}')
    pos.append(f'{l[l.index(p1[0]) + 1]}{int(p1[1]) + 2}')
if l.index(p1[0]) > 2:
    pos.append(f'{l[l.index(p1[0]) - 2]}{int(p1[1]) - 1}')
    pos.append(f'{l[l.index(p1[0]) - 2]}{int(p1[1]) + 1}')
if l.index(p1[0]) < 5:
    pos.append(f'{l[l.index(p1[0]) + 2]}{int(p1[1]) - 1}')
    pos.append(f'{l[l.index(p1[0]) + 2]}{int(p1[1]) + 1}')
if p2 in pos:
    print('VALIDO')
else:
    print('INVALIDO')