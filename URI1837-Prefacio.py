x = input().split()
a = int(x[0])
b = int(x[1])
q = a // b
r = a % b
if r < 0:
    r += abs(b)
    q += 1
print(q, r)