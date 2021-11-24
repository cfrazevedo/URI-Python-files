n = int(input())
b = c = 0
for _ in range(n):
    s = input().split()
    if s[1] == 'F':
        b += 1
    elif s[1] == 'M':
        c += 1
print(f'{c} carrinhos')
print(f'{b} bonecas')