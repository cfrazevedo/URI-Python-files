qt = int(input())
s = []
for d in range(0, qt):
    p = input().split()
    pi = input().split()
    sn = int(pi[0]) + int(pi[1])
    if sn % 2 == 0 and str(p[1].upper()) == 'PAR' or sn % 2 == 1 and str(p[1].upper()) == 'IMPAR':
        s.append(str(p[0]))
    else:
        s.append(str(p[2]))
for d in s:
    print(d)