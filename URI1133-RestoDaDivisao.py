x = int(input())
y = int(input())
if y < x:
    a = y
    b = x
else:
    b = y
    a = x
for c in range(a + 1, b):
    if c % 5 == 2 or c % 5 == 3:
        print(c)