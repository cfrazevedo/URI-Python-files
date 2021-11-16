abc = 'abcdefghijklmnopqrstuvwxyz'
k = input()
n = int(input())
for c in range(n):
    msg = input().split()
    crip = []
    i = 0
    for palavra in msg:
        if palavra[0] in 'aeiou':
            crip.append(palavra)
        else:
            pf = ''
            for letra in palavra:
                pf += abc[(abc.index(k[i % len(k)]) + abc.index(letra)) % 26]
                i += 1
            crip.append(pf)
    print(' '.join(crip))