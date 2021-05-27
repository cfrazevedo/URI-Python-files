c = int(input())
s = []
for d in range(0, c):
    n = int(input())
    if n % 2 == 0:
        s.append(0)
    else:
        s.append(1)
for d in s:
    print(d)