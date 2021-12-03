# NÃO RESOLVIDO

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
for c in range(int((n / 2) + 1)):
    nv += 6 * c
g = Grafo(nv, n)
for d in range(n):
    if d == 1:
        for e in range(6):
            g.adiciona_aresta(0, e + 1)
    elif d != 0 and d % 2 == 0:
        for e in range(6 * int((d - 1) / 2) + 1, 6 * int(d - 1)):
            g.adiciona_aresta(e, e + 1)
        g.adiciona_aresta(6 * int(d - 1), 6 * int((d - 1) / 2) + 1)
    elif d % 2 == 1:
        print(d)
        p = 6 * ((d - 2) // 2) + 1
        u = 6 * (d - 2)
        s = 0
        for e in range(p, u + 1):
            print(f's = {s}')
            g.adiciona_aresta(e, e + s + u)
            g.adiciona_aresta(e, e + s + u + 1)
            if e != p:
                g.adiciona_aresta(e, e + s + u - 1)
            s += 1
        g.adiciona_aresta(p, d * 6)

print(g.vertices)
g.mostra_matriz()
print(g.contar_adj())
g.passear()
print(g.caminhos)