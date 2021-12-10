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

    def custoRetorno(self, p, o):
        for i, c in enumerate(p):
            volta = {p}
            custo = 0
            #parei aqui pra calcular o retorno




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

print(*g.grafo, sep='\n')

g.pos = pos_or = vo[0][0]

for voo in vo:
    if g.pos not in voo:
        print(g.grafo[g.pos])
        for vert in g.grafo[g.pos].keys():
            if vert in voo:
                va = [g.pos, vert]
                g.viagem(va)
                break
    g.viagem(voo)

print(g.pos)
