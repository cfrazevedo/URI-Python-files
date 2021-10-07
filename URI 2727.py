abc = 'abcdefghijklmnopqrstuvwxyz'
while True:
    try:
        n = int(input())
        let = ''
        for t in range(n):
            cod = input().split()
            num = 0
            for c in cod:
                num = ((len(cod) - 1) * 3) + len(cod[0]) - 1
            let += abc[num]
        print(*let, sep='\n')
    except EOFError:
        break