n = int(input())
np = input().split()
t = 0
for c in range(0, n):
    if c == 0 or t > int(np[c]):
        t = int(np[c])
        r = c + 1
print(r)