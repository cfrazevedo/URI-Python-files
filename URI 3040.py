n = int(input())
for _ in range(n):
    h, d, g = [int(x) for x in input().split()]
    if 200 <= h <= 300 and d >= 50 and g >= 150:
        print('Sim')
    else:
        print('Nao')