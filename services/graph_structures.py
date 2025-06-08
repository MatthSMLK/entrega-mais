# services/graph_structures.py

import heapq
import collections
from abc import ABC, abstractmethod

class Grafo(ABC):
    """
    Classe base abstrata para garantir que todas as implementações de grafo
    tenham a mesma interface (mesmos métodos).
    """
    def __init__(self, cidades_nomes):
        self.nodes = list(cidades_nomes)
        self.node_map = {name: i for i, name in enumerate(self.nodes)}

    @abstractmethod
    def adicionar_aresta(self, u, v, peso):
        pass

    @abstractmethod
    def dijkstra(self, origem, use_heap=True):
        pass

    def obter_caminho(self, predecessores, destino_idx):
        """Reconstrói o caminho a partir do array de predecessores."""
        caminho_indices = []
        no_atual_idx = destino_idx
        while no_atual_idx is not None:
            caminho_indices.append(no_atual_idx)
            no_atual_idx = predecessores[no_atual_idx]
        
        # Converte índices de volta para nomes de cidades
        return [self.nodes[i] for i in reversed(caminho_indices)]

# --- IMPLEMENTAÇÃO 1: LISTA DE ADJACÊNCIA ---
class GrafoListaAdjacencia(Grafo):
    """Implementação do Grafo usando Lista de Adjacência (dicionário)."""
    def __init__(self, cidades_nomes):
        super().__init__(cidades_nomes)
        self.adj = collections.defaultdict(dict)

    def adicionar_aresta(self, u, v, peso):
        self.adj[u][v] = peso
        self.adj[v][u] = peso

    def dijkstra(self, origem_nome, use_heap=True):
        """
        Implementação do Dijkstra que pode usar HEAP (fila de prioridade) ou LISTA SIMPLES.
        Isso atende ao requisito de comparação.
        """
        distancias = {node: float('infinity') for node in self.nodes}
        predecessores = {node: None for node in self.nodes}
        distancias[origem_nome] = 0

        if use_heap:
            # --- Otimização com HEAP (Fila de Prioridade) ---
            fila_prioridade = [(0, origem_nome)]
            while fila_prioridade:
                distancia_atual, no_atual = heapq.heappop(fila_prioridade)
                if distancia_atual > distancias[no_atual]:
                    continue
                for vizinho, peso in self.adj[no_atual].items():
                    if distancias[no_atual] + peso < distancias[vizinho]:
                        distancias[vizinho] = distancias[no_atual] + peso
                        predecessores[vizinho] = no_atual
                        heapq.heappush(fila_prioridade, (distancias[vizinho], vizinho))
        else:
            # --- Alternativa com LISTA SIMPLES ---
            visitados = set()
            nos_nao_visitados = list(self.nodes)
            while nos_nao_visitados:
                # Encontra o nó com menor distância na lista (menos eficiente)
                min_dist = float('infinity')
                no_atual = None
                for n in nos_nao_visitados:
                    if distancias[n] < min_dist:
                        min_dist = distancias[n]
                        no_atual = n
                
                if no_atual is None: break 
                
                nos_nao_visitados.remove(no_atual)
                visitados.add(no_atual)

                for vizinho, peso in self.adj[no_atual].items():
                    if distancias[no_atual] + peso < distancias[vizinho]:
                        distancias[vizinho] = distancias[no_atual] + peso
                        predecessores[vizinho] = no_atual
        
        return distancias, predecessores


# --- IMPLEMENTAÇÃO 2: MATRIZ DE ADJACÊNCIA ---
class GrafoMatrizAdjacencia(Grafo):
    """Implementação do Grafo usando Matriz de Adjacência."""
    def __init__(self, cidades_nomes):
        super().__init__(cidades_nomes)
        num_nodes = len(self.nodes)
        self.matriz = [[float('inf')] * num_nodes for _ in range(num_nodes)]
        for i in range(num_nodes):
            self.matriz[i][i] = 0

    def adicionar_aresta(self, u, v, peso):
        u_idx, v_idx = self.node_map[u], self.node_map[v]
        self.matriz[u_idx][v_idx] = peso
        self.matriz[v_idx][u_idx] = peso

    def dijkstra(self, origem_nome, use_heap=True): # O parâmetro use_heap não tem efeito aqui
        origem_idx = self.node_map[origem_nome]
        num_nodes = len(self.nodes)
        
        distancias = [float('inf')] * num_nodes
        distancias[origem_idx] = 0
        predecessores = [None] * num_nodes
        visitados = [False] * num_nodes

        for _ in range(num_nodes):
            # Encontra o vértice não visitado com a menor distância
            min_dist = float('inf')
            u = -1
            for i in range(num_nodes):
                if not visitados[i] and distancias[i] < min_dist:
                    min_dist = distancias[i]
                    u = i
            
            if u == -1: break
            visitados[u] = True

            # Atualiza as distâncias dos vizinhos
            for v in range(num_nodes):
                if self.matriz[u][v] != float('inf') and not visitados[v]:
                    nova_distancia = distancias[u] + self.matriz[u][v]
                    if nova_distancia < distancias[v]:
                        distancias[v] = nova_distancia
                        predecessores[v] = u
        
        # Converte resultados de volta para dicionários baseados em nomes
        dist_dict = {self.nodes[i]: distancias[i] for i in range(num_nodes)}
        pred_dict = {self.nodes[i]: self.nodes[predecessores[i]] if predecessores[i] is not None else None for i in range(num_nodes)}
        
        return dist_dict, pred_dict