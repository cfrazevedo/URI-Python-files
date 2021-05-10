lst = []
x = 1
while x !=2:
    while len(lst) != 2:
        n = float(input())
        if n < 0 or n > 10:
            print('nota invalida')
        else:
            lst.append(n)
    print(f'media = {(sum(lst) / 2):.2f}')
    lst.clear()
    print('novo calculo (1-sim 2-nao)')
    x = int(input())
    while x != 1 and x != 2:
        print('novo calculo (1-sim 2-nao)')
        x = int(input())
