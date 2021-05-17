lst = []
for c in range(0, 10):
    x = int(input())
    lst.append(x)
for c, d in enumerate(lst):
    if d <= 0:
        print(f'X[{c}] = 1')
    else:
        print(f'X[{c}] = {d}')