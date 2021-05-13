x = int(input())
z = int(input())
while z <= x:
    z = int(input())
s = 1
n = x
while n < z:
    n += x + s
    s += 1
print(s)