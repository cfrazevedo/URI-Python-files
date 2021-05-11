x = g = a = d = 0
while x != 4:
    x = int(input())
    while 0 > x > 5:
        x = int(input())
    if x == 1:
        a += 1
    elif x == 2:
        g += 1
    elif x == 3:
        d += 1
print('MUITO OBRIGADO')
print(f'Alcool: {a}')
print(f'Gasolina: {g}')
print(f'Diesel: {d}')