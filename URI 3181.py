# NÃO RESOLVIDO - WRONG ANSWER

n, c = map(int, input().split())
encontros = {}
for _ in range(c):
    a, b, y = map(int, input().split())
    if not y in encontros:
        encontros[y] = {a, b}
    else:
        encontros[y].update([a, b])
ano = 'Impossible'
anoa = 'Impossible'
sa = set()
sb = set()
for k,v in encontros.items():
    l = list(v)
    if len(sa) <= n * 1 / 3:
        sa.update(v)
        ano = anoa
    else:
        if len(sa) <= n * 2 / 3:
            if l[0] in sa or l[1] in sa:
                sa.update(v)
                sa.update(sb)
                sb = set()
                if len(sa) <= n * 2 / 3:
                    ano = anoa
                else:
                    ano = 'Impossible'
                    break
            else:
                sb.update(v)
        else:
            ano = 'Impossible'
            break
    anoa = int(k) + 1
print(ano)