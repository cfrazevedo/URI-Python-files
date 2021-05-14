n = int(input())
for c in range(0, n):
    x = int(input())
    p = 0
    for c in range(2, x):
        if x % c == 0:
            p = 1
    if p != 1:
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')