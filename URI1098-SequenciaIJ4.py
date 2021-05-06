i = 0
j = 1
while i <= 2:
    for c in range(0, 3):
        if int(j):
            print(f'I={i} J={j}')
        else:
            print(f'I={i:.1f} J={j:.1f}')
        j += 1
    i += 0.2
    j -= 2.8
    if int(i) == round(i, 1):
        i = int(i)
    else:
        i = round(i, 1)
    if int(j) == round(j, 1):
        j = int(j)
    else:
        j = round(j, 1)