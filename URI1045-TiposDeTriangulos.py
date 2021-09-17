linha = input().split()
lst = sorted([float(linha[0]), float(linha[1]), float(linha[2])], reverse=True)
a = lst[0]
b = lst[1]
c = lst[2]
if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if (a ** 2) == (b ** 2) + (c ** 2):
        print('TRIANGULO RETANGULO')
    elif (a ** 2) > (b ** 2) + (c ** 2):
        print('TRIANGULO OBTUSANGULO')
    elif (a ** 2) < (b ** 2) + (c ** 2):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')