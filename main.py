# main.py

import time
from data.dados_cidades import cidades_nomes, centros_distribuicao_nomes, arestas
from models.cidade import Cidade
from models.entrega import Entrega
from services.graph import Grafo
from services.roteirizador import Roteirizador

def run_simulation():
    """
    Função principal que orquestra a simulação completa.
    1. Cria o grafo com as cidades e rotas.
    2. Instancia o roteirizador.
    3. Define e executa diferentes cenários de teste.
    """
    print("===================================================")
    print("  Iniciando Simulação de Otimização Logística ")
    print("===================================================\n")

    # 1. Montagem do Grafo
    cidades = {nome: Cidade(nome) for nome in cidades_nomes}
    grafo = Grafo()
    for u, v, peso in arestas:
        grafo.adicionar_aresta(u, v, peso)

    # --- CENÁRIO 1: Poucas entregas e rotas curtas  ---
    print("\n--- Cenário 1: Entregas Iniciais (Volume Baixo) ---")
    roteirizador_c1 = Roteirizador(grafo, centros_distribuicao_nomes, num_caminhoes_por_cd=3)
    entregas_cenario1 = [
        Entrega(cidades["Natal"], 500, 2),
        Entrega(cidades["Goiania"], 800, 1),
        Entrega(cidades["Rio de Janeiro"], 1200, 2),
    ]
    start_time_c1 = time.time()
    roteirizador_c1.processar_entregas(entregas_cenario1)
    end_time_c1 = time.time()
    print(f"\nTempo de execução do Cenário 1: {end_time_c1 - start_time_c1:.4f} segundos.")
    print("-" * 60)

    # --- CENÁRIO 2: Muitas entregas e rotas longas  ---
    print("\n--- Cenário 2: Volume Maior de Entregas ---")
    roteirizador_c2 = Roteirizador(grafo, centros_distribuicao_nomes, num_caminhoes_por_cd=4)
    entregas_cenario2 = [
        Entrega(cidades["Manaus"], 100, 5),
        Entrega(cidades["Porto Alegre"], 1500, 3),
        Entrega(cidades["Curitiba"], 900, 2),
        Entrega(cidades["Salvador"], 800, 2),
        Entrega(cidades["Joao Pessoa"], 500, 1),
        Entrega(cidades["Belo Horizonte"], 950, 2),
        Entrega(cidades["Campo Grande"], 750, 3),
        Entrega(cidades["Sao Paulo"], 1000, 1),
        Entrega(cidades["Goiania"], 1500, 1),
    ]
    start_time_c2 = time.time()
    roteirizador_c2.processar_entregas(entregas_cenario2)
    end_time_c2 = time.time()
    print(f"\nTempo de execução do Cenário 2: {end_time_c2 - start_time_c2:.4f} segundos.")
    print("-" * 60)
    
    # --- CENÁRIO 3: Teste de restrição com caminhões limitados ---
    print("\n--- Cenário 3: Entregas com Caminhões Limitados ---")
    roteirizador_c3 = Roteirizador(grafo, centros_distribuicao_nomes, num_caminhoes_por_cd=1)
    entregas_cenario3 = [
        Entrega(cidades["Natal"], 1500, 1),
        Entrega(cidades["Salvador"], 1800, 2),
        Entrega(cidades["Goiania"], 1200, 1),
        Entrega(cidades["Porto Alegre"], 1000, 2),
        Entrega(cidades["Curitiba"], 900, 1),
    ]
    start_time_c3 = time.time()
    roteirizador_c3.processar_entregas(entregas_cenario3)
    end_time_c3 = time.time()
    print(f"\nTempo de execução do Cenário 3: {end_time_c3 - start_time_c3:.4f} segundos.")
    print("-" * 60)

    print("\n===================================================")
    print("      Simulação Concluída!      ")
    print("===================================================\n")

if __name__ == "__main__":
    run_simulation()