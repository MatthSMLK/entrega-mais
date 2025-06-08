# services/graph.py

import heapq
import collections

class Grafo:
    """
    Representa o mapa de rotas como um grafo ponderado.
    Utiliza uma lista de adjacência (dicionário de dicionários) para armazenar as arestas.
    Essa estrutura é eficiente para grafos esparsos, como um mapa de estradas.
    """
    def __init__(self):
        self.adj = collections.defaultdict(dict)

    def adicionar_aresta(self, u, v, peso):
        """Adiciona uma aresta bidirecional entre os nós 'u' and 'v' com um 'peso' (distância)."""
        self.adj[u][v] = peso
        self.adj[v][u] = peso

    def dijkstra(self, origem):
        """
        Implementação do algoritmo de Dijkstra para encontrar os caminhos mais curtos
        de um nó de 'origem' para todos os outros nós no grafo.
        
        Utiliza uma fila de prioridade (min-heap) para otimização, garantindo a escolha
        do vértice mais próximo a cada passo de forma eficiente.

        Retorna:
            distancias (dict): Dicionário com as distâncias mínimas da origem a cada cidade.
            predecessores (dict): Dicionário para reconstruir o caminho mais curto.
        """
        distancias = {node: float('infinity') for node in self.adj}
        predecessores = {node: None for node in self.adj}
        distancias[origem] = 0
        
        # Fila de prioridade armazena (distância, nó)
        fila_prioridade = [(0, origem)]

        while fila_prioridade:
            distancia_atual, no_atual = heapq.heappop(fila_prioridade)

            if distancia_atual > distancias[no_atual]:
                continue

            for vizinho, peso in self.adj[no_atual].items():
                distancia = distancia_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    predecessores[vizinho] = no_atual
                    heapq.heappush(fila_prioridade, (distancia, vizinho))
        
        return distancias, predecessores

    def obter_caminho(self, predecessores, destino):
        """Reconstrói o caminho do destino de volta à origem a partir do dict de predecessores."""
        caminho = []
        no_atual = destino
        while no_atual is not None:
            caminho.append(no_atual)
            no_atual = predecessores[no_atual]
        return caminho[::-1] # Retorna o caminho da origem ao destino