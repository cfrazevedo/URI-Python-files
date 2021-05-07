lst = []
while True:
    l1 = input().split()
    a = int(l1[0])
    b = int(l1[1])
    if a == b:
        break
    else:
        if a < b:
            lst.append('Crescente')
        elif a > b:
            lst.append('Decrescente')
for c in lst:
    print(c)