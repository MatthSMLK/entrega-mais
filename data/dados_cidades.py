# data/dados_cidades.py

# Lista de todas as cidades (CDs e destinos) no nosso sistema.
cidades_nomes = [
    "Belem", "Recife", "Brasilia", "Sao Paulo", "Florianopolis",
    "Natal", "Joao Pessoa", "Salvador", "Goiania", "Rio de Janeiro",
    "Curitiba", "Porto Alegre", "Fortaleza", "Belo Horizonte", "Manaus",
    "Campo Grande"
]

# Definição dos Centros de Distribuição conforme o problema.
centros_distribuicao_nomes = [
    "Belem", "Recife", "Brasilia", "Sao Paulo", "Florianopolis"
]

# Arestas do grafo no formato (origem, destino, peso/distância em km).
# Estas são as "distâncias reais" que o grafo usará.
# As distâncias são simulações para criar um grafo conectado.
arestas = [
    ("Belem", "Manaus", 1450), ("Belem", "Fortaleza", 1600), ("Belem", "Brasilia", 2100),
    ("Fortaleza", "Recife", 800), ("Recife", "Natal", 300), ("Recife", "Joao Pessoa", 120),
    ("Recife", "Salvador", 850), ("Salvador", "Brasilia", 1450), ("Salvador", "Belo Horizonte", 1400),
    ("Brasilia", "Goiania", 210), ("Brasilia", "Sao Paulo", 1000), ("Brasilia", "Belo Horizonte", 740),
    ("Brasilia", "Campo Grande", 1130), ("Belo Horizonte", "Rio de Janeiro", 440),
    ("Belo Horizonte", "Sao Paulo", 580), ("Sao Paulo", "Rio de Janeiro", 430),
    ("Sao Paulo", "Curitiba", 410), ("Sao Paulo", "Campo Grande", 1000),
    ("Curitiba", "Florianopolis", 300), ("Curitiba", "Porto Alegre", 710),
    ("Florianopolis", "Porto Alegre", 480)
]