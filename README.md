# Entrega+ – Simulador de logística inteligente

Este projeto simula cenários logísticos para avaliação de desempenho em redes de entrega entre grandes cidades brasileiras. O sistema executa diferentes simulações e apresenta comparativos para tomada de decisão estratégica.

## Objetivo

Criar um simulador que permita:
- Avaliar desempenho de diferentes cenários logísticos.
- Simular situações de carga normal e cenários de estresse.
- Apresentar um resumo comparativo dos resultados obtidos.

## Cidades simuladas

- Belém  
- Recife  
- Brasília  
- São Paulo  
- Florianópolis

## Estrutura do projeto

```
entrega_mais/
├── main.py
├── simulation/
│   ├── simulation_runner.py
│   ├── scenarios.py
│   └── reporter.py
└── README.md
```

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
- O projeto é individual e segue as orientações do professor.
