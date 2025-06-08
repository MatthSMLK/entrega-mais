# main.py (Versão Interativa com Sumário Final)

import time
from data.dados_cidades import cidades_nomes
from models.cidade import Cidade
from models.entrega import Entrega
from simulation.simulation_runner import SimulationRunner

def imprimir_sumario_comparativo(titulo, resultados):
    """
    Imprime uma tabela formatada com o resumo dos tempos de execução,
    destacando o mais rápido e a diferença percentual dos outros.
    """
    print("\n" + "="*70)
    print(f"  {titulo.upper()}  ")
    print("="*70)
    
    if not resultados:
        print("Nenhum resultado para exibir.")
        return

    # Ordena os resultados pelo tempo total para fácil comparação
    resultados_ordenados = sorted(resultados, key=lambda x: x['total_time'])
    mais_rapido = resultados_ordenados[0]
    
    print(f"{'Configuração':<45} | {'Tempo Total (s)':<15} | {'Diferença'}")
    print("-" * 70)

    # Imprime o mais rápido primeiro
    print(f"{mais_rapido['config']:<45} | {mais_rapido['total_time']:<15.6f} | {'(O mais rápido)'}")

    # Imprime os outros, calculando a diferença percentual
    for res in resultados_ordenados[1:]:
        diferenca_percentual = ((res['total_time'] / mais_rapido['total_time']) - 1) * 100
        diff_str = f"+{diferenca_percentual:.2f}% mais lento"
        print(f"{res['config']:<45} | {res['total_time']:<15.6f} | {diff_str}")
    
    print("=" * 70)


def main():
    """
    Ponto de entrada principal. Executa simulações em modo interativo
    e apresenta um sumário comparativo no final.
    """
    # Listas para armazenar os resultados de cada cenário
    resultados_cenario_pequeno = []
    resultados_cenario_grande = []

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

    # --- Execução do Cenário Pequeno ---
    print("\n>>> INICIANDO CENÁRIO DE TESTE: VOLUME BAIXO DE ENTREGAS <<<")
    sim_runner_pequeno = SimulationRunner(entregas_cenario_pequeno, num_caminhoes_por_cd=3)
    
    res = sim_runner_pequeno.run(graph_type='lista', use_heap=True)
    resultados_cenario_pequeno.append(res)
    input("\n--> Pressione Enter para rodar a próxima comparação...")
    
    res = sim_runner_pequeno.run(graph_type='lista', use_heap=False)
    resultados_cenario_pequeno.append(res)
    input("\n--> Pressione Enter para rodar a próxima comparação...")
    
    res = sim_runner_pequeno.run(graph_type='matriz')
    resultados_cenario_pequeno.append(res)
    input("\n--> Pressione Enter para iniciar o cenário com ALTO VOLUME de entregas...")


    # --- Execução do Cenário Grande ---
    print("\n>>> INICIANDO CENÁRIO DE TESTE: VOLUME ALTO DE ENTREGAS <<<")
    sim_runner_grande = SimulationRunner(entregas_cenario_grande, num_caminhoes_por_cd=4)
    
    res = sim_runner_grande.run(graph_type='lista', use_heap=True)
    resultados_cenario_grande.append(res)
    input("\n--> Pressione Enter para rodar a próxima comparação...")
    
    res = sim_runner_grande.run(graph_type='lista', use_heap=False)
    resultados_cenario_grande.append(res)
    input("\n--> Pressione Enter para rodar a última comparação...")
    
    res = sim_runner_grande.run(graph_type='matriz')
    resultados_cenario_grande.append(res)

    # --- APRESENTAÇÃO DO SUMÁRIO FINAL ---
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário de Volume Baixo", resultados_cenario_pequeno)
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário de Volume Alto", resultados_cenario_grande)

    print("\n\nAnálise de Desempenho Concluída!")


if __name__ == "__main__":
    main()