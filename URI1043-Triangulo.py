linha1 = input().split()
a = float(linha1[0])
b = float(linha1[1])
c = float(linha1[2])
if a >= b + c or b >= a + c or c >= a + b:
    print(f'Area = {(((a + b) * c) / 2):.1f}')
else:
    print(f'Perimetro = {(a + b + c):.1f}')