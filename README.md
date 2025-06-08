# Entrega+ – Simulador de logística inteligente

SOBRE
Este projeto é uma solução algorítmica desenvolvida para otimizar o processo de roteamento de entregas de uma empresa de logística fictícia. O objetivo principal é minimizar o tempo e a distância percorrida pelos caminhões, garantindo que cada entrega parta do centro de distribuição (CD) mais próximo do seu destino final e que as restrições operacionais (capacidade de carga, horas de trabalho) sejam respeitadas.

O núcleo do projeto consiste na modelagem do problema utilizando grafos e na aplicação do algoritmo de Dijkstra para o cálculo de rotas mais curtas, além de uma análise de desempenho comparativa entre diferentes estruturas de dados.

## Objetivo

Criar um simulador que permita:
- Avaliar desempenho de diferentes cenários logísticos.
- Simular situações de carga normal e cenários de estresse.
- Apresentar um resumo comparativo dos resultados obtidos.

## Funcionalidades principais

Modelagem orientada a objetos: O sistema modela cidades, entregas (com peso e prazo), caminhões (com capacidade e limite de horas) e o próprio grafo de rotas.

Roteirização inteligente: Utiliza o algoritmo de Dijkstra para calcular a rota mais curta a partir do centro de distribuição mais próximo de cada destino.

Análise de desempenho comparativa: O projeto foi estruturado para testar e comparar o desempenho de diferentes abordagens, conforme solicitado nos requisitos da avaliação:
Grafo implementado com Lista de Adjacência vs. Matriz de Adjacência.

Algoritmo de Dijkstra otimizado com Fila de Prioridade (Heap) vs. uma busca em Lista Simples.
Execução interativa e relatório final: O script principal roda de forma interativa, pausando após cada teste para permitir a análise dos resultados, e exibe um sumário comparativo completo no final.

## Cidades simuladas

- Belém  
- Recife  
- Brasília  
- São Paulo  
- Florianópolis

## Estrutura do projeto

```
entrega_mais/
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
|-- README.md                 # Detalhes pertinentes
```

## Tecnologias utilizadas

Python 3
Bibliotecas padrão do Python (time, collections, heapq).

## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Abra um terminal e vá até a pasta onde está o projeto.
3. Execute o seguinte comando:

```bash
python main.py
```
Se não executar dessa forma, apenas clique no botão no canto superior direito no VScode
dentro da "main.py" (Run Python File).

Durante a execução, você poderá acompanhar os testes de desempenho com entrada interativa e visualizar o resumo final no terminal.

## Notas

- O código está organizado em módulos para facilitar a leitura e manutenção.
- Foram incluídos cenários pequenos, grandes e de estresse para simular diferentes cargas de trabalho.
- O projeto é individual.

## Informações da disciplina

Este trabalho foi desenvolvido como parte da avaliação A3 para a Unidade curricular digital de Estrutura de dados e análise de algoritmos.

Professor: Glauber Galvão
Semestre: 2025.1
Aluno: Matheus Silva Leite
RA: 12316020