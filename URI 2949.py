n = int(input())
a = e = h = m = x = 0
for _ in range(n):
    p = input().split()
    if p[1] == 'A':
        a += 1
    elif p[1] == 'E':
        e += 1
    elif p[1] == 'H':
        h += 1
    elif p[1] == 'M':
        m += 1
    elif p[1] == 'X':
        x += 1
print(f'{x} Hobbit(s)')
print(f'{h} Humano(s)')
print(f'{e} Elfo(s)')
print(f'{a} Anao(s)')
print(f'{m} Mago(s)')