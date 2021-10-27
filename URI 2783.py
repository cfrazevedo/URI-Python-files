n, c, m = [int(x) for x in input().split()]
xi = [int(x) for x in input().split()]
yi = [int(x) for x in input().split()]
x = xi[:]
for f in xi:
    if f in yi:
        x.remove(f)
print(len(x))