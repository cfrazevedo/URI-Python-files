c = int(input())
t = str(input()).upper()
v = []
for linha in range(0, 12):
    for coluna in range(0, 12):
        x = float(input())
        if coluna == c:
            v.append(x)
if t == 'S':
    print(f'{(sum(v)):.1f}')
elif t == 'M':
    print(f'{(sum(v) / len(v)):.1f}')