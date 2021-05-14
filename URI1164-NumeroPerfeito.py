n = int(input())
for c in range(0, n):
    x = int(input())
    ln = []
    for c in range(1, x):
        if x % c == 0:
            ln.append(c)
    if x == sum(ln):
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')