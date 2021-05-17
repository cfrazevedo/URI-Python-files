t = int(input())
x = 0
y = 1
fb = [x, y]
lst = []
for c in range (0, 61):
    f = y + x
    x = y
    y = f
    fb.append(f)
for c in range (0, t):
    n = int(input())
    lst.append(n)
for c in lst:
    print(f'Fib({c}) = {fb[c]}')