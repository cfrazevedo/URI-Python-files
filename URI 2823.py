n = int(input())
u = []
for _ in range(n):
    c, p = [int(x) for x in input().split()]
    u.append(c / p)
if sum(u) <= 1:
    print('OK')
else:
    print('FAIL')