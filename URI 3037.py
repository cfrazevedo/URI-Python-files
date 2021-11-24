n = int(input())
for _ in range(n):
    m = j = 0
    for _ in range(3):
        x, d = [int(x) for x in input().split()]
        j += x * d
    for _ in range(3):
        x, d = [int(x) for x in input().split()]
        m += x * d
    if m > j:
        print('MARIA')
    elif j > m:
        print('JOAO')