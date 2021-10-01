n = int(input())
palavras = []
for c in range(n):
    palavras.append(input())
q = int(input())
for c in range(q):
    np = maior = 0
    p = input()
    for d in palavras:
        if p == d[:len(p)]:
            np += 1
            if len(d) > maior:
                maior = len(d)
    if np == 0:
        print(-1)
    else:
        print(np, maior)
