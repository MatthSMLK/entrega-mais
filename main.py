# main.py (Versão final refatorada e limpa)

from simulation.simulation_runner import SimulationRunner
from simulation.scenarios import get_scenarios
from simulation.reporter import imprimir_sumario_comparativo

def main():
    """
    Ponto de entrada principal da aplicação.
    Orquestra a execução das simulações e a apresentação dos resultados,
    delegando as responsabilidades para módulos específicos.
    """
    # Listas para armazenar os resultados
    resultados_pequeno = []
    resultados_grande = []
    
    # Carrega os cenários de teste a partir do módulo de cenários
    cenarios = get_scenarios()
    entregas_pequeno = cenarios["cenario_pequeno"]
    entregas_grande = cenarios["cenario_grande"]
    
    print("=========================================================")
    print("   Projeto de Otimização Logística - Análise de Desempenho   ")
    print("=========================================================\n")
    print("O script será executado em modo interativo.")
    input("--> Pressione Enter para iniciar a simulação...")

    # --- Execução do Cenário Pequeno ---
    print("\n>>> INICIANDO CENÁRIO DE TESTE: VOLUME BAIXO DE ENTREGAS <<<")
    sim_runner_pequeno = SimulationRunner(entregas_pequeno, num_caminhoes_por_cd=3)
    
    for config in [('lista', True), ('lista', False), ('matriz', True)]:
        res = sim_runner_pequeno.run(graph_type=config[0], use_heap=config[1])
        resultados_pequeno.append(res)
        if config != ('matriz', True):
            input("\n--> Pressione Enter para a próxima comparação...")

    input("\n--> Pressione Enter para iniciar o cenário com ALTO VOLUME de entregas...")

    # --- Execução do Cenário Grande ---
    print("\n>>> INICIANDO CENÁRIO DE TESTE: VOLUME ALTO DE ENTREGAS <<<")
    sim_runner_grande = SimulationRunner(entregas_grande, num_caminhoes_por_cd=4)
    
    for config in [('lista', True), ('lista', False), ('matriz', True)]:
        res = sim_runner_grande.run(graph_type=config[0], use_heap=config[1])
        resultados_grande.append(res)
        if config != ('matriz', True):
            input("\n--> Pressione Enter para a próxima comparação...")

    # --- Apresentação do Sumário Final ---
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário de Volume Baixo", resultados_pequeno)
    imprimir_sumario_comparativo("Sumário Comparativo - Cenário de Volume Alto", resultados_grande)

    print("\n\nAnálise de Desempenho Concluída!")


if __name__ == "__main__":
    main()