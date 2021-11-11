n = int(input())
x = 1
y = 1
fb = [str(x), str(y)]
for c in range(2, 41):
    f = y + x
    x = y
    y = f
    fb.append(str(f))
fb.reverse()
print(*fb[41 - n:])