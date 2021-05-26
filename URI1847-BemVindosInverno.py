x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
x = b - a
y = c - b
if x > 0:
    if y >= x:
        print(':)')
    else:
        print(':(')
else:
    if y > x:
        print(':)')
    else:
        print(':(')