lst = []
x = 1
while x !=2:
    n = input().split()
    i = int(n[0])
    g = int(n[1])
    if i > g:
        lst.append('inter')
    elif i < g:
        lst.append('gremio')
    elif i == g:
        lst.append('empate')
    print('Novo grenal (1-sim 2-nao)')
    x = int(input())
    while x != 1 and x != 2:
        print('Novo grenal (1-sim 2-nao)')
        x = int(input())
print(f'{len(lst)} grenais')
print(f'Inter:{lst.count("inter")}')
print(f'Gremio:{lst.count("gremio")}')
print(f'Empates:{lst.count("empate")}')
if lst.count("inter") > lst.count("gremio"):
    print('Inter venceu mais')
elif lst.count("inter") < lst.count("gremio"):
    print('Gremio venceu mais')
elif lst.count("inter") < lst.count("gremio"):
    print('Nao houve vencedor')