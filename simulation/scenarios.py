# simulation/scenarios.py

import random
from models.cidade import Cidade
from models.entrega import Entrega
from data.dados_cidades import cidades_nomes, centros_distribuicao_nomes

def get_scenarios():
    """
    Prepara e retorna os cenários de teste com volumes de entrega
    Baixo (10), Médio (50) e de Estresse (150).
    """
    cidades = {nome: Cidade(nome) for nome in cidades_nomes}
    destinos_possiveis = [c for c in cidades_nomes if c not in centros_distribuicao_nomes]

    # --- Cenário de Baixo Volume ---
    entregas_cenario_baixo = []
    random.seed(42) # Semente para reprodutibilidade
    for i in range(10):
        destino = random.choice(destinos_possiveis)
        peso = random.randint(100, 2000)
        prazo = random.randint(2, 6)
        entregas_cenario_baixo.append(Entrega(cidades[destino], peso, prazo))

    # --- Cenário de Médio Volume ---
    entregas_cenario_medio = []
    random.seed(84) # Semente diferente para um novo conjunto
    for i in range(50):
        destino = random.choice(destinos_possiveis)
        peso = random.randint(100, 2000)
        prazo = random.randint(2, 6)
        entregas_cenario_medio.append(Entrega(cidades[destino], peso, prazo))
    
    # --- Cenário de Estresse (Alto Volume) ---
    entregas_cenario_estresse = []
    random.seed(126) # Semente diferente para um terceiro conjunto
    for i in range(150):
        destino = random.choice(destinos_possiveis)
        peso = random.randint(100, 2000)
        prazo = random.randint(2, 6)
        entregas_cenario_estresse.append(Entrega(cidades[destino], peso, prazo))

    return {
        "cenario_baixo": entregas_cenario_baixo,
        "cenario_medio": entregas_cenario_medio,
        "cenario_estresse": entregas_cenario_estresse
    }