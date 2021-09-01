l = [int(x) for x in input().split()]
l.sort()
if l[0] + l[1] > l[2]:
    if l[0] == l[1] == l[2]:
        print('Valido-Equilatero')
    elif l[0] == l[1] or l[1] == l[2]:
        print('Valido-Isoceles')
    else:
        print('Valido-Escaleno')
    if (l[0] ** 2) + (l[1] ** 2) == (l[2] ** 2):
        print('Retangulo: S')
    else:
        print('Retangulo: N')
else:
    print('Invalido')