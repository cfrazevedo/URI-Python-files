t = int(input())
lst = []
for c in range(0, t):
    p = []
    l = input().split()
    p.append(int(l[0]))
    p.append(int(l[1]))
    lst.append(p[:])
for c in lst:
    print(sum(c))