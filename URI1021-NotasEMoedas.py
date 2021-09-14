v = float(input())
n = [100, 50, 20, 10, 5, 2]
m = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for c in n:
    qn = int(v / c)
    print(f'{qn} nota(s) de R$ {c:.2f}')
    v -= c * qn
print('MOEDAS:')
for c in m:
    qm = int(round(v, 2) / c)
    print(f'{qm} moeda(s) de R$ {c:.2f}')
    v -= c * qm