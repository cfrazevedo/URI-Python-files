lst = []
x = int(input())
for c in range(0, 10):
    if c == 0:
        lst.append(x)
    else:
        x *= 2
        lst.append(x)
for c, d in enumerate(lst):
    print(f'N[{c}] = {d}')