n = int(input())
x = input().split()
xx = []
t = 0
e = 0
for c in range(0, n):
    xx.append(int(x[c]))
while 0 <= t < n:
    if xx[t] == 0:
        break
    xx[t] -= 1
    if xx[t] % 2 == 1:
        t -= 1
    else:
        t += 1
for c in range(0, n):
    if int(x[c]) != xx[c]:
        e += 1
print(f'{e} {sum(xx)}')