# simulation/simulation_runner.py

import time
from services.roteirizador import Roteirizador
from services.graph_structures import GrafoListaAdjacencia, GrafoMatrizAdjacencia
from data.dados_cidades import cidades_nomes, centros_distribuicao_nomes, arestas

class SimulationRunner:
    """
    Orquestra a execução de simulações com diferentes configurações
    para permitir a comparação de desempenho.
    """
    def __init__(self, entregas, num_caminhoes_por_cd):
        self.entregas = entregas
        self.num_caminhoes_por_cd = num_caminhoes_por_cd

    def run(self, graph_type='lista', use_heap=True):
        """
        Executa uma única simulação com a configuração especificada.
        
        :param graph_type: 'lista' para Lista de Adjacência, 'matriz' para Matriz de Adjacência.
        :param use_heap: True para usar heap no Dijkstra (se aplicável), False para usar lista simples.
        """
        print("-" * 70)
        config_str = f"Grafo: {graph_type.upper()} | Dijkstra com: {'HEAP' if use_heap else 'LISTA SIMPLES'}"
        print(f"Executando simulação com configuração: {config_str}")

        # 1. Escolha e construção da estrutura do grafo
        start_build_time = time.time()
        if graph_type == 'lista':
            grafo = GrafoListaAdjacencia(cidades_nomes)
        elif graph_type == 'matriz':
            grafo = GrafoMatrizAdjacencia(cidades_nomes)
        else:
            raise ValueError("Tipo de grafo inválido. Use 'lista' ou 'matriz'.")
        
        for u, v, peso in arestas:
            grafo.adicionar_aresta(u, v, peso)
        build_time = time.time() - start_build_time
        
        # 2. Execução do roteirizador
        roteirizador = Roteirizador(grafo, centros_distribuicao_nomes, self.num_caminhoes_por_cd)
        
        start_process_time = time.time()
        resultados, alocadas, nao_alocadas = roteirizador.processar_entregas(self.entregas, use_heap)
        process_time = time.time() - start_process_time
        
        # 3. Exibição dos resultados
        print("\n--- Resumo da Simulação ---")
        print(f"Tempo de construção do grafo: {build_time:.6f} segundos.")
        print(f"Tempo de processamento das entregas: {process_time:.6f} segundos.")
        print(f"Tempo Total: {build_time + process_time:.6f} segundos.")
        print(f"Entregas alocadas: {alocadas}/{len(self.entregas)}")
        print(f"Entregas não alocadas: {len(nao_alocadas)}")
        
        # Imprime uma tabela com os resultados detalhados
        print("\n--- Log de Rotas ---")
        header = f"{'Destino':<15} | {'Alocado':<7} | {'CD Partida':<15} | {'Distancia (km)':<15} | {'Rota'}"
        print(header)
        print("-" * len(header))
        for res in resultados:
            print(f"{res['Destino']:<15} | {res['Alocado']:<7} | {res['CD Partida']:<15} | {res['Distancia (km)']:<15.2f} | {res['Caminho']}")
        print("-" * 70 + "\n")

        return {
            "config": config_str,
            "build_time": build_time,
            "process_time": process_time,
            "total_time": build_time + process_time
        }