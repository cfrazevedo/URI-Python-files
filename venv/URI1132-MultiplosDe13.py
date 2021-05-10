x = int(input())
y = int(input())
s = 0
if x > y:
    a = y
    b = x
else:
    a = x
    b = y
for c in range(a, b + 1):
    if c % 13 != 0:
        s += c
print(s)