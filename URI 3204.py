# NÃO RESOLVIDO
# TIME LIMITED EXCEEDED

class Grafo:


    def __init__(self, vertices, passos):
        self.vertices = vertices
        self.passos = passos
        self.caminhos = 0
        self.grafo = [[] for _ in range(self.vertices)]


    def adiciona_aresta(self, x, v):
        self.grafo[x].append(v)
        self.grafo[v].append(x)

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(f'{i} = {self.grafo[i]}')

    def contar_adj(self):
        con = 0
        for i in range(self.vertices):
            con += len(self.grafo[i])
        return con

    def passear(self):
        p = self.passos - 1
        self.darPasso(0, p)

    def darPasso(self, i, p):
        if p == 0:
            if 0 in self.grafo[i]:
                self.caminhos += 1
        else:
            for c in self.grafo[i]:
                self.darPasso(c, p - 1)



n = int(input())
nv = 1
limites = []
for c in range(int((n / 2) + 1)):
    nv += 6 * c
    limites.append(nv)
g = Grafo(nv, n)
for d in range(n):
    if d == 1:
        for e in range(6):
            g.adiciona_aresta(0, e + 1)
    elif d != 0 and d % 2 == 0:
        a = limites[(d // 2) - 1]
        b = limites[d // 2] - 1
        for e in range(a, b):
            g.adiciona_aresta(e, e + 1)
        g.adiciona_aresta(a, b)
    elif d % 2 == 1:
        p = limites[(d // 2) - 1]
        u = limites[d // 2] - 1
        s = p + (6 * (d//2))
        for e in range(p, u + 1):
            g.adiciona_aresta(e, s)
            if e != p:
                g.adiciona_aresta(e, s - 1)
            if (e - 1) % (d // 2) == 0:
                g.adiciona_aresta(e, s + 1)
                s += 1
            s += 1
        g.adiciona_aresta(p, s - 1)

g.passear()
print(g.caminhos)