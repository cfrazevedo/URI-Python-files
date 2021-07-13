n = int(input())
a = {}
for c in range(0, n):
    no = str(input())
    gd = float(input())
    l = [float(x) for x in input().split()]
    l.sort()
    l.remove(l[len(l) - 1])
    l.remove(l[0])
    a[no] = gd * sum(l)
for d, e in a.items():
    print(f'{d} {e:.2f}')