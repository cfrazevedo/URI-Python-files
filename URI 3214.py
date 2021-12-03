e, f, c = map(int, input().split())
v = e + f
b = 0
while v >= c:
    v -= c - 1
    b += 1
print(b)