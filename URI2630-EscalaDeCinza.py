t = int(input())
for c in range(t):
    p = 0
    conv = input()
    r, g, b = [int(x) for x in input().split()]
    if conv == 'eye':
        p = (0.3 * r) + (0.59 * g) + (0.11 * b)
    elif conv == 'mean':
        p = (r + g + b) / 3
    elif conv == 'max':
        p = max(r, g, b)
    elif conv == 'min':
        p = min(r, g, b)
    print(f'Caso #{c + 1}: {int(p)}')