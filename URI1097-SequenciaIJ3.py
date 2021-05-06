i = 1
j = 7
k = 0
while True:
    print(f'I={i} J={j}')
    if i == 9 and k == 2:
        break
    elif k != 2:
        j -= 1
        k += 1
    else:
        i += 2
        j += 4
        k = 0