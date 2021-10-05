# EXERCÍCIO NÃO RESOLVIDO
# PROBLEMAS DE "TIME LIMIT EXCEEDED"
# ACEITO SUGESTÕES

while True:
    try:
        n = int(input())
        x = [int(z) for z in input().split()]
        y = 0
        for c in range(1, n):
            d = abs(sum(x[:c]) - sum(x[c:]))
            if c == 1 or d < y:
                y = d
            else:
                break
        print(y)
    except EOFError:
        break