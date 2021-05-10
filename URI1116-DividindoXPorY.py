n = int(input())
lst = []
for c in range(0, n):
    l1 = input().split()
    a = int(l1[0])
    b = int(l1[1])
    if b == 0:
        lst.append('divisao impossivel')
    else:
        lst.append(a / b)
for c in lst:
    print(c)
