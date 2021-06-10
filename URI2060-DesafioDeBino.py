n = int(input())
l = input().split()
m2 = 0
m3 = 0
m4 = 0
m5 = 0
for c in range(0, n):
    if int(l[c]) % 2 == 0:
        m2 += 1
    if int(l[c]) % 3 == 0:
        m3 += 1
    if int(l[c]) % 4 == 0:
        m4 += 1
    if int(l[c]) % 5 == 0:
        m5 += 1
print(f'{m2} Multiplo(s) de 2')
print(f'{m3} Multiplo(s) de 3')
print(f'{m4} Multiplo(s) de 4')
print(f'{m5} Multiplo(s) de 5')