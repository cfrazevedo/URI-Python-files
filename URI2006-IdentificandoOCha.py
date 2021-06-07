t = int(input())
rp = input().split()
rc = 0
for c in rp:
    if t == int(c):
        rc += 1
print(rc)