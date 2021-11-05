n = int(input())
s = s1 = b = b1 = a = a1 = 0
for c in range(0, n):
    no = str(input())
    si, bi, ai = [int(x) for x in input().split()]
    s1i, b1i, a1i = [int(x) for x in input().split()]
    s += si
    s1 += s1i
    b += bi
    b1 += b1i
    a += ai
    a1 += a1i
print(f'Pontos de Saque: {(s1 / s) * 100:.2f} %.')
print(f'Pontos de Bloqueio: {(b1 / b) * 100:.2f} %.')
print(f'Pontos de Ataque: {(a1 / a) * 100:.2f} %.')