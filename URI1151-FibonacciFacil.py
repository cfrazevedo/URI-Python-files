n = int(input())
x = 0
y = 1
fb = [x, y]
for c in range(2, 46):
    f = y + x
    x = y
    y = f
    fb.append(f)
for c in range(0, n):
    if c == n - 1:
        print(fb[c])
    else:
        print(fb[c], end=' ')
