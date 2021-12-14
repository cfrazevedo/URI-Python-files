l = input().split()
n = int(l[0])
m = int(l[1])
for c in range(0, m):
    a = str(input())
    if a == 'fechou':
        n += 1
    elif a == 'clicou':
        n -= 1
print(n)