i = 1
j = 7
while True:
    print(f'I={i} J={j}')
    if i == 9 and j == 5:
        break
    elif j != 5:
        j -= 1
    else:
        i += 2
        j = 7