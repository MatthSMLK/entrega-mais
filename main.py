# main.py (Versão Interativa)

from data.dados_cidades import cidades_nomes
from models.cidade import Cidade
from models.entrega import Entrega
# O caminho aqui pode precisar de ajuste dependendo da sua estrutura de pastas
# Se simulation_runner.py estiver dentro de uma pasta 'simulation', o import abaixo está correto.
from simulation.simulation_runner import SimulationRunner

def main():
    """
    Ponto de entrada principal. Executa as simulações em modo interativo,
    pausando após cada teste para permitir a explicação dos resultados.
    """
    print("=========================================================")
    print("   Projeto de Otimização Logística - Análise de Desempenho   ")
    print("=========================================================\n")
    print("O script será executado em modo interativo.")
    print("Após cada simulação, pressione Enter para continuar para a próxima.")
    input("--> Pressione Enter para iniciar a primeira simulação...")

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
    print("\n>>> INICIANDO CENÁRIO DE TESTE: VOLUME BAIXO DE ENTREGAS <<<")
    sim_runner_pequeno = SimulationRunner(entregas_cenario_pequeno, num_caminhoes_por_cd=3)
    
    # 1. Lista de Adjacência + Heap (Sua implementação original)
    sim_runner_pequeno.run(graph_type='lista', use_heap=True)
    input("\n--> Pressione Enter para rodar a próxima comparação...")
    
    # 2. Lista de Adjacência + Lista Simples
    sim_runner_pequeno.run(graph_type='lista', use_heap=False)
    input("\n--> Pressione Enter para rodar a próxima comparação...")
    
    # 3. Matriz de Adjacência
    sim_runner_pequeno.run(graph_type='matriz')
    input("\n--> Pressione Enter para iniciar o cenário com ALTO VOLUME de entregas...")


    # --- Execução do Cenário Grande com todas as configurações ---
    print("\n>>> INICIANDO CENÁRIO DE TESTE: VOLUME ALTO DE ENTREGAS <<<")
    sim_runner_grande = SimulationRunner(entregas_cenario_grande, num_caminhoes_por_cd=4)
    
    # 1. Lista de Adjacência + Heap
    sim_runner_grande.run(graph_type='lista', use_heap=True)
    input("\n--> Pressione Enter para rodar a próxima comparação...")
    
    # 2. Lista de Adjacência + Lista Simples
    sim_runner_grande.run(graph_type='lista', use_heap=False)
    input("\n--> Pressione Enter para rodar a última comparação...")
    
    # 3. Matriz de Adjacência
    sim_runner_grande.run(graph_type='matriz')

    print("\n=========================================================")
    print("           Análise de Desempenho Concluída!           ")
    print("=========================================================")


if __name__ == "__main__":
    main()