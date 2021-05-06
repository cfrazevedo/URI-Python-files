a1 = str(input())
b1 = str(input())
w1 = int(a1[-2] + a1[-1])
x1 = int(b1[0] + b1[1])
y1 = int(b1[5] + b1[6])
z1 = int(b1[10] + b1[11])
a2 = str(input())
b2 = str(input())
w2 = int(a2[-2] + a2[-1])
x2 = int(b2[0] + b2[1])
y2 = int(b2[5] + b2[6])
z2 = int(b2[10] + b2[11])
if z1 > z2:
    z2 += 60
    y2 -= 1
if y1 > y2:
    y2 += 60
    x2 -= 1
if x1 > x2:
    x2 += 24
    w2 -= 1
print(f'{w2 - w1} dia(s)')
print(f'{x2 - x1} hora(s)')
print(f'{y2 - y1} minuto(s)')
print(f'{z2 - z1} segundo(s)')