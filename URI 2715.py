# EXERCÍCIO NÃO RESOLVIDO
# PROBLEMAS DE "TIME LIMIT EXCEEDED"
# ACEITO SUGESTÕES

while True:
    try:
        n = int(input())
        x = [int(z) for z in input().split()]
        s = sum(x)
        g = 0
        for _ in range(n - 1):
            if g < sum(x):
                g += x.pop()
            else:
                break
        r = s - g
        y = abs(g - r)
        print(y)
    except EOFError:
        break