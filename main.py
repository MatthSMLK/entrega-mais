# main.py (Versão final com Cenário de Estresse)

from simulation.simulation_runner import SimulationRunner
from simulation.scenarios import get_scenarios
from simulation.reporter import imprimir_sumario_comparativo

def main():
    """
    Ponto de entrada principal da aplicação.
    Orquestra a execução das simulações, incluindo um cenário de estresse,
    e a apresentação dos resultados.
    """
    # Listas para armazenar os resultados
    resultados_pequeno = []
    resultados_grande = []
    resultados_estresse = []
    
    # Carrega os cenários de teste
    cenarios = get_scenarios()
    
    print("=========================================================")
    print("   Projeto de Otimização Logística - Análise de Desempenho   ")
    print("=========================================================\n")
    print("O script será executado em modo interativo.")
    input("--> Pressione Enter para iniciar a simulação...")

    # --- Execução do Cenário Pequeno ---
    print("\n>>> CENÁRIO 1: VOLUME BAIXO DE ENTREGAS <<<")
    runner_pequeno = SimulationRunner(cenarios["cenario_pequeno"], num_caminhoes_por_cd=3)
    for config in [('lista', True), ('lista', False), ('matriz', True)]:
        res = runner_pequeno.run(graph_type=config[0], use_heap=config[1])
        resultados_pequeno.append(res)
        if config != ('matriz', True): input("\n--> Pressione Enter...")

    # --- Execução do Cenário Grande ---
    input("\n--> Pressione Enter para iniciar o cenário de ALTO VOLUME...")
    print("\n>>> CENÁRIO 2: VOLUME ALTO DE ENTREGAS <<<")
    runner_grande = SimulationRunner(cenarios["cenario_grande"], num_caminhoes_por_cd=4)
    for config in [('lista', True), ('lista', False), ('matriz', True)]:
        res = runner_grande.run(graph_type=config[0], use_heap=config[1])
        resultados_grande.append(res)
        if config != ('matriz', True): input("\n--> Pressione Enter...")

    # --- Execução do Cenário de Estresse ---
    input("\n--> Pressione Enter para iniciar o CENÁRIO DE ESTRESSE...")
    print("\n>>> CENÁRIO 3: ESTRESSE COM 50 ENTREGAS ALEATÓRIAS <<<")
    runner_estresse = SimulationRunner(cenarios["cenario_estresse"], num_caminhoes_por_cd=10) # Mais caminhões
    for config in [('lista', True), ('lista', False), ('matriz', True)]:
        res = runner_estresse.run(graph_type=config[0], use_heap=config[1])
        resultados_estresse.append(res)
        if config != ('matriz', True): input("\n--> Pressione Enter...")

    # --- APRESENTAÇÃO DO SUMÁRIO FINAL ---
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário Pequeno", resultados_pequeno)
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário Grande", resultados_grande)
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário de Estresse (50 Entregas)", resultados_estresse)

    print("\n\nAnálise de Desempenho Concluída!")


if __name__ == "__main__":
    main()