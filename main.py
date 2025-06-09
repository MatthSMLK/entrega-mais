# main.py (Versão final com Cenários Robustos)

from simulation.simulation_runner import SimulationRunner
from simulation.scenarios import get_scenarios
from simulation.reporter import imprimir_sumario_comparativo

def main():
    """
    Ponto de entrada principal da aplicação.
    Orquestra a execução de múltiplos cenários de teste (baixo, médio e alto volume)
    e apresenta um sumário comparativo de desempenho no final.
    """
    # Listas para armazenar os resultados
    resultados_baixo = []
    resultados_medio = []
    resultados_estresse = []
    
    # Carrega os cenários de teste
    cenarios = get_scenarios()
    
    print("=========================================================")
    print("   Projeto de Otimização Logística - Análise de Desempenho   ")
    print("=========================================================\n")
    print("O script executará 3 cenários de teste (10, 50 e 150 entregas).")
    input("--> Pressione Enter para iniciar a simulação...")

    # --- Execução do Cenário de Baixo Volume ---
    print("\n>>> CENÁRIO 1: BAIXO VOLUME (10 ENTREGAS) <<<")
    runner_baixo = SimulationRunner(cenarios["cenario_baixo"], num_caminhoes_por_cd=5)
    for config in [('lista', True), ('lista', False), ('matriz', True)]:
        res = runner_baixo.run(graph_type=config[0], use_heap=config[1])
        resultados_baixo.append(res)
        if config != ('matriz', True): input("\n--> Pressione Enter...")

    # --- Execução do Cenário de Médio Volume ---
    input("\n--> Pressione Enter para iniciar o cenário de MÉDIO VOLUME...")
    print("\n>>> CENÁRIO 2: MÉDIO VOLUME (50 ENTREGAS) <<<")
    runner_medio = SimulationRunner(cenarios["cenario_medio"], num_caminhoes_por_cd=15) # Mais caminhões
    for config in [('lista', True), ('lista', False), ('matriz', True)]:
        res = runner_medio.run(graph_type=config[0], use_heap=config[1])
        resultados_medio.append(res)
        if config != ('matriz', True): input("\n--> Pressione Enter...")

    # --- Execução do Cenário de Estresse (Alto Volume) ---
    input("\n--> Pressione Enter para iniciar o CENÁRIO DE ESTRESSE...")
    print("\n>>> CENÁRIO 3: ALTO VOLUME (150 ENTREGAS) <<<")
    runner_estresse = SimulationRunner(cenarios["cenario_estresse"], num_caminhoes_por_cd=40) # Mais caminhões
    for config in [('lista', True), ('lista', False), ('matriz', True)]:
        res = runner_estresse.run(graph_type=config[0], use_heap=config[1])
        resultados_estresse.append(res)
        if config != ('matriz', True): input("\n--> Pressione Enter...")

    # --- APRESENTAÇÃO DO SUMÁRIO FINAL ---
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário de Baixo Volume (10 Entregas)", resultados_baixo)
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário de Médio Volume (50 Entregas)", resultados_medio)
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário de Alto Volume (150 Entregas)", resultados_estresse)

    print("\n\nAnálise de Desempenho Concluída!")


if __name__ == "__main__":
    main()