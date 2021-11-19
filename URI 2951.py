n, g = [int(x) for x in input().split()]
rv = dict()
for _ in range(n):
    r, v = input().split()
    rv[r] = int(v)
x = int(input())
runas = input().split()
v = 0
for c in range(x):
    v += rv[runas[c]]
print(v)
if v < g:
    print('My precioooous')
else:
    print('You shall pass!')