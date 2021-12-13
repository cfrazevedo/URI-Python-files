"""
URI (BEE) 3204 - NÃO RESOLVIDO - TIME LIMIT ERROR

Não sei como resolve este exercício sem analisar todos os passeios percorridos pela larva.
O código abaixo faz isso e chega nos resultados esperados, entretanto gasta muito tempo e
memória (Time Limit Error). Meu PC levou mais de 1h para processar os limítrofes 14 passos.

Vi alguns devs resolvendo este problema associando diretamente o número de passos com o
número de passeios, sem analisar cada passeio, ou seja, não resolve o problema.

Como o número máximo de passos é 14, fica fácil receber o aceite do julgamento.
O programa que recebe o aceite do BEE(URI) vou disponibilizar em 'URI 3204(1).py'
"""


class Grafo:
    """
    Este grafo ira delinear os passeios pelo favo

    Ele deve ser composto, não direcionado, regular e sem laço.
    """

    def __init__(self, vertices, passos, limites):
        self.vertices = vertices
        self.passos = passos
        self.passeios = 0  # passeios que retornam ao vértice original #0
        self.grafo = [[] for _ in range(self.vertices)]
        self.limites = limites

    def adiciona_aresta(self, x, v):
        """
        Algoritmo de formação de arestas

        :param x: Vértice 1
        :param v: Vértice 2
        """
        self.grafo[x].append(v)
        self.grafo[v].append(x)

    def passear(self, p, i=0):
        '''
        Analisando os caminhos
        
        :param p: número de passos a percorrer
        :param i: casa (vértice) onde a larva se encontra
        '''
        if p == 1:  # faltando um passo para ternimar o passeio
            if 0 in self.grafo[i]:  # se o vértice tem aresta para #0
                self.passeios += 1  # é registrado
        else:  # passo por passo analisado
            try:
                l = self.limites[p]
            except:
                l = self.vertices
            if i < l:  # o "l" impede (otimiza) a análise de passeios q não retornam a #0 com passos restantes
                for c in self.grafo[i]:
                    if c < l:
                        self.passear(p - 1, c)


t = int(input())
for _ in range(t):
    n = int(input())
    nro_vertices = 1
    limites = []  # lista com o número de vértices até determinada camada (definida pelo índice)

    for c in range(int((n / 2) + 1)):
        nro_vertices += 6 * c
        limites.append(nro_vertices)
    g = Grafo(nro_vertices, n, limites)
    # criação do grafo - rede de casas (vértices) e suas conexões (arestas)

    for d in range(n):  # criando as arestas do grafo
        if d == 1:  # o vértice original #0 se liga com os seis externos imediatos (#1 a #6)
            for e in range(6):
                g.adiciona_aresta(0, e + 1)

        elif d % 2 == 1:  # os vértices externos se ligam com seus vizinhos internos imediatos
            p = limites[(d // 2) - 1]
            u = limites[d // 2] - 1
            s = p + (6 * (d // 2))
            for e in range(p, u + 1):
                g.adiciona_aresta(e, s)
                if e != p:
                    g.adiciona_aresta(e, s - 1)
                if (e - 1) % (d // 2) == 0:
                    g.adiciona_aresta(e, s + 1)
                    s += 1
                s += 1
            g.adiciona_aresta(p, s - 1)

        elif d != 0 and d % 2 == 0:  # os vértices externos se ligar com seus vizinhos externos
            a = limites[(d // 2) - 1]
            b = limites[d // 2] - 1
            for e in range(a, b):
                g.adiciona_aresta(e, e + 1)
            g.adiciona_aresta(a, b)

    g.passear(n)  # iniciando a analise de todos os passeios até o retorno a #0 com n passos
    print(g.passeios)  # imprime o número de passeios que retornam a #0 com n passos
