e = input().split()
s = int(e[0])
t = int(e[1])
f = int(e[2])
x = s + t + f
if x >= 24:
    x -= 24
elif x < 0:
    x += 24
print(x)