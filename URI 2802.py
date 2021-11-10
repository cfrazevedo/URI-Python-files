n = int(input())
a = 1
b = 1
while a != n:
    x = 1
    for c in range(a, n):
        b += x
        x += a - 1
    a += 1
print(b)