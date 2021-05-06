c = 0
s = 0
r = 0
l1 = int(input())
for d in range(0, l1):
    lc = input().split()
    if str(lc[1]) == 'C':
        c += int(lc[0])
    elif str(lc[1]) == 'S':
        s += int(lc[0])
    elif str(lc[1]) == 'R':
        r += int(lc[0])
t = c + s + r
print(f'Total: {t} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {(c * 100 / t):.2f} %')
print(f'Percentual de ratos: {(r * 100 / t):.2f} %')
print(f'Percentual de sapos: {(s * 100 / t):.2f} %')