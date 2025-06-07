# main.py

from data.distancias import cidades, centros_distribuicao
from model.entrega import Entrega
from controller.roteirizador import processar_entregas

# Lista de entregas simuladas
entregas = [
    Entrega(cidades["Natal"], 500, 2),
    Entrega(cidades["Salvador"], 1200, 3),
    Entrega(cidades["Goiania"], 800, 1),
    Entrega(cidades["Porto Alegre"], 1900, 4),
    Entrega(cidades["Curitiba"], 2500, 2),  # Vai falhar por excesso de peso
]

# Executar o processo de alocação
processar_entregas(entregas, centros_distribuicao)
