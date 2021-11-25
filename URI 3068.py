teste = 0
while True:
    teste += 1
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    n = int(input())
    m = 0
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        if x1 <= x <= x2 and y2 <= y <= y1:
            m += 1
    print(f'Teste {teste}')
    print(m)