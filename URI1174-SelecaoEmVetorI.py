lst = []
for c in range(0, 100):
    x = float(input())
    lst.append(x)
for c, d in enumerate(lst):
    if d <= 10:
        print(f'A[{c}] = {d:.1f}')