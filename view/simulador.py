# view/simulador.py

import time # Para medir o tempo de execução dos cenários
from data.distancias import cidades, centros_distribuicao
from model.entrega import Entrega
from controller.roteirizador import Roteirizador

def simular():
    """
    Função principal que orquestra a simulação de otimização logística.
    Define diferentes cenários de entregas para avaliar o desempenho do algoritmo.
    """
    print("===================================================")
    print("  Iniciando Simulação de Otimização Logística ")
    print("  com Múltiplos Centros de Distribuição          ")
    print("===================================================\n")

    # Instancia o roteirizador com os centros de distribuição e um número padrão de caminhões por CD.
    # O número de caminhões por CD pode ser ajustado para diferentes cenários de teste.
    roteirizador = Roteirizador(centros_distribuicao, num_caminhoes_por_cd=3)

    # --- CENÁRIO 1: Entregas Iniciais (Volume Pequeno/Médio) ---
    print("\n--- Cenário 1: Entregas Iniciais (Volume Pequeno/Médio) ---")
    entregas_cenario1 = [
        Entrega(cidades["Natal"], 500, 2),
        Entrega(cidades["Salvador"], 1200, 3),
        Entrega(cidades["Goiania"], 800, 1),
        Entrega(cidades["Porto Alegre"], 1900, 4),
        Entrega(cidades["Curitiba"], 2500, 2), # Exemplo para testar excesso de peso/tempo
        Entrega(cidades["Joao Pessoa"], 700, 1),
        Entrega(cidades["Rio de Janeiro"], 1000, 2),
    ]
    start_time_c1 = time.time()
    roteirizador.processar_entregas(entregas_cenario1)
    end_time_c1 = time.time()
    print(f"\nTempo de execução do Cenário 1: {end_time_c1 - start_time_c1:.4f} segundos.")
    print("-" * 60)

    # --- CENÁRIO 2: Volume Maior de Entregas ---
    print("\n--- Cenário 2: Volume Maior de Entregas ---")
    entregas_cenario2 = [
        Entrega(cidades["Natal"], 300, 1),
        Entrega(cidades["Salvador"], 800, 2),
        Entrega(cidades["Goiania"], 600, 1),
        Entrega(cidades["Porto Alegre"], 1500, 3),
        Entrega(cidades["Curitiba"], 2000, 2),
        Entrega(cidades["Joao Pessoa"], 500, 1),
        Entrega(cidades["Rio de Janeiro"], 900, 1),
        Entrega(cidades["Belem"], 400, 1),
        Entrega(cidades["Brasilia"], 700, 2),
        Entrega(cidades["Florianopolis"], 1800, 3),
        Entrega(cidades["Fortaleza"], 650, 1),
        Entrega(cidades["Belo Horizonte"], 950, 2),
        Entrega(cidades["Manaus"], 100, 5), # Entrega mais distante, pode ter problema de prazo/tempo
        Entrega(cidades["Campo Grande"], 750, 2),
        Entrega(cidades["Sao Paulo"], 1000, 1), # Entrega local de CD
        Entrega(cidades["Recife"], 300, 1), # Entrega local de CD
        Entrega(cidades["Goiania"], 1500, 1), # Outra entrega para Goiania, testando capacidade
    ]
    # Para este cenário, podemos usar um roteirizador novo ou resetar o existente se quisermos simular um "novo dia"
    # Vamos criar um novo para ter frotas resetadas
    roteirizador_cenario2 = Roteirizador(centros_distribuicao, num_caminhoes_por_cd=4) # Mais caminhões
    start_time_c2 = time.time()
    roteirizador_cenario2.processar_entregas(entregas_cenario2)
    end_time_c2 = time.time()
    print(f"\nTempo de execução do Cenário 2: {end_time_c2 - start_time_c2:.4f} segundos.")
    print("-" * 60)

    # --- Cenário 3: Entregas com Caminhões Limitados (Teste de Restrição) ---
    print("\n--- Cenário 3: Entregas com Caminhões Limitados ---")
    entregas_cenario3 = [
        Entrega(cidades["Natal"], 1500, 1),
        Entrega(cidades["Salvador"], 1800, 2),
        Entrega(cidades["Goiania"], 2200, 1), # Provável que falhe por peso/tempo
        Entrega(cidades["Porto Alegre"], 1000, 2),
        Entrega(cidades["Curitiba"], 900, 1),
    ]
    # Roteirizador com poucos caminhões para forçar falhas de alocação
    roteirizador_cenario3 = Roteirizador(centros_distribuicao, num_caminhoes_por_cd=1)
    start_time_c3 = time.time()
    roteirizador_cenario3.processar_entregas(entregas_cenario3)
    end_time_c3 = time.time()
    print(f"\nTempo de execução do Cenário 3: {end_time_c3 - start_time_c3:.4f} segundos.")
    print("-" * 60)


    print("\n===================================================")
    print("  Simulação de Otimização Logística Concluída!  ")
    print("===================================================\n")

    # --- NOTAS SOBRE AVALIAÇÃO DE DESEMPENHO E ESTRUTURAS DE DADOS ---
    # Conforme o requisito, o projeto pede para comparar o desempenho
    # usando diferentes estruturas de dados (lista simples vs. heap, matriz de adjacência vs. lista de adjacência).
    #
    # Nesta implementação, as distâncias são calculadas dinamicamente com base nas coordenadas euclidianas.
    # A busca pelo "centro mais próximo" utiliza uma iteração sobre a lista de CDs,
    # que para um número pequeno de CDs (5) é eficiente.
    #
    # Para uma demonstração mais aprofundada de comparação de estruturas (e para um grafo mais complexo
    # onde Dijkstra realmente performaria um roteamento entre múltiplos pontos),
    # seria necessário:
    # 1. Implementar uma representação de grafo explícita (e.g., dicionário de dicionários ou matriz de adjacência)
    #    e outra com lista de adjacência.
    # 2. Implementar o algoritmo de Dijkstra utilizando uma fila de prioridade (heap).
    # 3. Rodar os mesmos cenários com ambas as implementações do grafo/Dijkstra e comparar os tempos de execução
    #    e consumo de memória para justificar a escolha mais eficiente.
    #
    # Dada a limitação de tempo e experiência mencionada, a solução atual foca em:
    # - Modelagem clara das entidades (Cidades, Entregas, Caminhões).
    # - Identificação do CD mais próximo.
    # - Verificação de capacidade e tempo dos caminhões.
    # - Simulação de alocação.
    # - Teste com diferentes cenários.
    #
    # O tempo de execução medido acima reflete o desempenho da lógica atual de iteração e cálculo de distância.
    # No relatório, você pode discutir conceitualmente as vantagens de cada estrutura e
    # como elas seriam aplicadas para otimizar o algoritmo em uma escala maior.