o = str(input()).upper()
v = []
for linha in range(0, 12):
    for coluna in range(0, 12):
        x = float(input())
        if coluna > linha and coluna + linha < 11:
            v.append(x)
if o == 'S':
    print(f'{(sum(v)):.1f}')
elif o == 'M':
    print(f'{(sum(v) / len(v)):.1f}')