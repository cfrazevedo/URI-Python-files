s = 0
for c in range(0, 39):
    s += ((2 * c) + 1) / (2 ** c)
print(f'{s:.2f}')