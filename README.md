Projeto de otimização logística com múltiplos centros de distribuição

Sobre o projeto
Este projeto é uma solução algorítmica desenvolvida para otimizar o processo de roteamento de entregas de uma empresa de logística fictícia. O objetivo principal é minimizar o tempo e a distância percorrida pelos caminhões, garantindo que cada entrega parta do centro de distribuição (CD) mais próximo do seu destino final e que as restrições operacionais (capacidade de carga, horas de trabalho) sejam respeitadas.

O núcleo do projeto consiste na modelagem do problema utilizando grafos e na aplicação do algoritmo de Dijkstra para o cálculo de rotas mais curtas, além de uma análise de desempenho comparativa entre diferentes estruturas de dados.

Funcionalidades principais
Modelagem orientada a objetos: O sistema modela Cidades, Entregas (com peso e prazo), Caminhões (com capacidade e limite de horas) e o próprio Grafo de rotas.

Roteirização inteligente: Utiliza o algoritmo de Dijkstra para calcular a rota mais curta a partir do Centro de Distribuição mais próximo de cada destino.

Análise de desempenho comparativa: O projeto foi estruturado para testar e comparar o desempenho de diferentes abordagens, conforme solicitado nos requisitos da avaliação:

Grafo implementado com lista de adjacência vs. Matriz de adjacência.
Algoritmo de Dijkstra otimizado com fila de prioridade (Heap) vs. uma busca em lista simples.

Execução interativa e relatório final: O script principal roda de forma interativa, pausando após cada teste para permitir a análise dos resultados, e exibe um sumário comparativo completo no final.

Estrutura de pastas
O projeto foi organizado de forma modular para separar as responsabilidades, seguindo boas práticas de engenharia de software.

/
|-- data/
|   |-- dados_cidades.py      # Define as cidades, CDs e arestas do grafo
|-- models/
|   |-- caminhao.py           # Modelo do caminhão
|   |-- cidade.py             # Modelo da cidade
|   |-- entrega.py            # Modelo da entrega
|-- services/
|   |-- graph_structures.py   # Implementações do grafo (Lista e Matriz)
|   |-- roteirizador.py       # Lógica principal de roteirização e alocação
|-- simulation/
|   |-- simulation_runner.py  # Orquestrador que executa uma simulação
|   |-- scenarios.py          # Define os cenários de teste (volume baixo/alto)
|   |-- reporter.py           # Gera o sumário comparativo final
|-- main.py                   # Ponto de entrada principal da aplicação
|-- README.md                 # Este arquivo

Tecnologias utilizadas
Python 3
Bibliotecas padrão do Python (time, collections, heapq).

Como executar
Certifique-se de ter o Python 3 instalado.
Navegue até a pasta raiz do projeto pelo terminal.

Execute o seguinte comando:
Bash (Ctrl + ') no VScode

python main.py
O script será iniciado em modo interativo. Pressione Enter para avançar entre as diferentes etapas da simulação.

Ao final, serão exibidas duas tabelas com o sumário comparativo de desempenho para os cenários de baixo e alto volume de entregas.
Informações da disciplina
Este trabalho foi desenvolvido como parte da avaliação A3 para a Unidade curricular digital de Estrutura de dados e Análise de algoritmos.

Professor: Glauber Galvão
Semestre: 2025.1
