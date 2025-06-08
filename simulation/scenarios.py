# simulation/scenarios.py

import random
from models.cidade import Cidade
from models.entrega import Entrega
from data.dados_cidades import cidades_nomes, centros_distribuicao_nomes

def get_scenarios():
    """
    Prepara e retorna os cenários de teste, incluindo um cenário de estresse
    com um grande número de entregas geradas aleatoriamente.
    """
    cidades = {nome: Cidade(nome) for nome in cidades_nomes}

    # Cenário Pequeno (para demonstração inicial)
    entregas_cenario_pequeno = [
        Entrega(cidades["Natal"], 500, 2),
        Entrega(cidades["Goiania"], 800, 1),
    ]

    # Cenário Grande (volume médio)
    entregas_cenario_grande = [
        Entrega(cidades["Manaus"], 100, 5),
        Entrega(cidades["Porto Alegre"], 1500, 3),
        Entrega(cidades["Curitiba"], 900, 2),
        Entrega(cidades["Salvador"], 800, 2),
        Entrega(cidades["Joao Pessoa"], 500, 1),
        Entrega(cidades["Belo Horizonte"], 950, 2),
        Entrega(cidades["Cuiaba"], 750, 3), # Usando nova cidade
    ]
    
    # Cenário de Estresse (volume alto, para acentuar diferenças de performance)
    entregas_cenario_estresse = []
    destinos_possiveis = [c for c in cidades_nomes if c not in centros_distribuicao_nomes]
    for _ in range(50):  # Gerando 50 entregas aleatórias
        destino = random.choice(destinos_possiveis)
        peso = random.randint(100, 2000)
        prazo = random.randint(1, 5)
        entregas_cenario_estresse.append(Entrega(cidades[destino], peso, prazo))

    return {
        "cenario_pequeno": entregas_cenario_pequeno,
        "cenario_grande": entregas_cenario_grande,
        "cenario_estresse": entregas_cenario_estresse
    }