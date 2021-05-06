n = int(input())
l = []
for c in range(0, n):
    x = (input().split())
    x1 = float(x[0]) * 2
    x2 = float(x[1]) * 3
    x3 = float(x[2]) * 5
    l.append((x1 + x2 + x3) / 10)
for c in l:
    print(f'{c:.1f}')