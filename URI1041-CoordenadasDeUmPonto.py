linha1 = input().split()
x = float(linha1[0])
y = float(linha1[1])
if x == y == 0:
    print('Origem')
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo X')
if x > 0:
    if y > 0:
        print('Q1')
    elif y < 0:
        print('Q4')
elif x < 0:
    if y > 0:
        print('Q2')
    elif y < 0:
        print('Q3')