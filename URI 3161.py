n, m = [int(x) for x in input().split()]
frutas = []
come = []
for _ in range(n):
    frutas.append(input().lower())
l = ''
for _ in range(m):
    l += input().lower()
lr = l[::-1]
for f in frutas:
    if f in l or f in lr:
        come.append(f)
for f in frutas:
    if f in come:
        print(f'Sheldon come a fruta {f}')
    else:
        print(f'Sheldon detesta a fruta {f}')