lst = []
while True:
    l1 = input().split()
    a = int(l1[0])
    b = int(l1[1])
    if a == 0 or b == 0:
        break
    else:
        if a > 0 and b > 0:
            lst.append('primeiro')
        elif a > 0 and b < 0:
            lst.append('quarto')
        elif a < 0 and b < 0:
            lst.append('terceiro')
        elif a < 0 and b > 0:
            lst.append('segundo')
for c in lst:
    print(c)