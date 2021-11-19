n = int(input())
v1 = int(input())
e = 'S'
for _ in range(1, n):
    v = int(input())
    if v > v1:
        e = 'N'
print(e)