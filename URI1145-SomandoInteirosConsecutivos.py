a = input().split()
x = int(a[0])
y = 0
for c in range(0, len(a)):
    if c != 0 and int(a[c]) > 0:
        y = int(a[c])
        break
s = 0
for c in range (x, y + x):
    s += c
print(s)