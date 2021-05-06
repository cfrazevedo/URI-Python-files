l1 = int(input())
l2 = []
for c in range(0, l1):
    l3 = input().split()
    a = int(l3[0])
    b = int(l3[1])
    if a <= b:
        x = a
        y = b
    else:
        x = b
        y = a
    soma = 0
    for d in range(x + 1, y):
        if d % 2 == 1:
            soma += d
    l2.append(soma)
for c in l2:
    print(c)