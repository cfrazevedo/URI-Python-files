# NÃO RESOLVIDO

from math import inf

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [{} for _ in range(self.vertices)]
        self.custo = 0
        self.pos = 0

    def addAresta(self, u, v, p):
        self.grafo[u - 1][v] = p
        self.grafo[v - 1][u] = p

    def viagem(self, aresta):
        if self.pos == aresta[0]:
            self.pos = aresta[1]
        elif self.pos == aresta[1]:
            self.pos = aresta[0]
        self.custo += self.grafo[aresta[0] - 1][aresta[1]]

    def custoViagem(self, origem, destino, custo = 0, volta = ''):
        volta += str(origem)
        custof = inf
        for k, v in self.grafo[origem - 1].items():
            print(f'volta :{volta}')
            print(f'destino: {k}')
            if not str(k) in volta:
                if k == destino:
                    print('destino alcançado')
                    if custo < custof:
                        custo += v
                        custof = custo
                        break
                else:
                    try:
                        print(f'viajando para {destino}')
                        self.custoViagem(k, destino, custo + v, volta)
                    except:
                        pass
        return custof


n, r1 = map(int, input().split())

g = Grafo(n)
vo = []

for _ in range(r1):
    a, b, c = map(int, input().split())
    g.addAresta(a, b, c)
    vo.append([a, b])

r2 = int(input())
for _ in range(r2):
    a, b, c = map(int, input().split())
    g.addAresta(a, b, c)

print(*[(f'{i + 1}: {j}') for i, j in enumerate(g.grafo)], sep='\n')

g.pos = pos_or = vo[0][0]

for voo in vo:
    if g.pos not in voo:
        voou = False
        for vert, custo in g.grafo[g.pos].items():
            if vert in voo:
                if not voou:
                    voou = True
                    v1 = vert
                    c1 = custo
                else:
                    if c1 > custo:
                        v1 = vert
                        c1 = custo
        if voou:
            va = [g.pos, v1]
            g.viagem([g.pos, v1])
        else:
            c1 = g.custoViagem(g.pos, voo[0])
            c2 = g.custoViagem(g.pos, voo[1])
            if c1 <= c2:
                g.custo += c1
                g.pos = voo[1]
            else:
                g.custo += c2
                g.pos = voo[1]
    g.viagem(voo)

print(g.custo)
print(g.custoViagem(g.pos, pos_or))
g.custo += g.custoViagem(g.pos, pos_or)
print(g.custo)
