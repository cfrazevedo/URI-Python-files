a = float(input())
n = p = 0
if a <= 400:
    n = a * 1.15
    p = 15
elif 400 < a <= 800:
    n = a * 1.12
    p = 12
elif 800 < a <= 1200:
    n = a * 1.10
    p = 10
elif 1200 < a <= 2000:
    n = a * 1.07
    p = 7
elif 2000 < a:
    n = a * 1.04
    p = 4
d = n - a
print(f'Novo salario: {n:.2f}\n'
      f'Reajuste ganho: {d:.2f}\n'
      f'Em percentual: {p} %')