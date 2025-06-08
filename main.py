# main.py

from data.dados_cidades import cidades_nomes
from models.cidade import Cidade
from models.entrega import Entrega
from simulation.simulation_runner import SimulationRunner

def main():
    """
    Ponto de entrada principal. Define os cenários e executa as simulações
    com diferentes estruturas de dados para comparação, conforme exigido pelo projeto.
    """
    print("=========================================================")
    print("   Projeto de Otimização Logística - Análise de Desempenho   ")
    print("=========================================================\n")

    cidades = {nome: Cidade(nome) for nome in cidades_nomes}

    # --- Definição dos Cenários ---
    entregas_cenario_pequeno = [
        Entrega(cidades["Natal"], 500, 2),
        Entrega(cidades["Goiania"], 800, 1),
        Entrega(cidades["Rio de Janeiro"], 1200, 2),
    ]

    entregas_cenario_grande = [
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

    # --- Execução do Cenário Pequeno com todas as configurações ---
    print(">>> INICIANDO CENÁRIO DE TESTE: VOLUME BAIXO DE ENTREGAS <<<")
    sim_runner_pequeno = SimulationRunner(entregas_cenario_pequeno, num_caminhoes_por_cd=3)
    
    # 1. Lista de Adjacência + Heap (Sua implementação original)
    sim_runner_pequeno.run(graph_type='lista', use_heap=True)
    
    # 2. Lista de Adjacência + Lista Simples
    sim_runner_pequeno.run(graph_type='lista', use_heap=False)
    
    # 3. Matriz de Adjacência
    sim_runner_pequeno.run(graph_type='matriz')


    # --- Execução do Cenário Grande com todas as configurações ---
    print("\n>>> INICIANDO CENÁRIO DE TESTE: VOLUME ALTO DE ENTREGAS <<<")
    sim_runner_grande = SimulationRunner(entregas_cenario_grande, num_caminhoes_por_cd=4)
    
    # 1. Lista de Adjacência + Heap
    sim_runner_grande.run(graph_type='lista', use_heap=True)
    
    # 2. Lista de Adjacência + Lista Simples
    sim_runner_grande.run(graph_type='lista', use_heap=False)
    
    # 3. Matriz de Adjacência
    sim_runner_grande.run(graph_type='matriz')

    print("=========================================================")
    print("           Análise de Desempenho Concluída!           ")
    print("=========================================================")
    print("Use os tempos de execução acima para escrever seu relatório e justificar a escolha da estrutura mais eficiente. ")


if __name__ == "__main__":
    main()