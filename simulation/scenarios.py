# simulation/scenarios.py

from models.cidade import Cidade
from models.entrega import Entrega
from data.dados_cidades import cidades_nomes

def get_scenarios():
    """
    Prepara e retorna os cenários de teste para a simulação.
    Isso centraliza a criação de dados de teste em um único local.
    """
    cidades = {nome: Cidade(nome) for nome in cidades_nomes}

    entregas_cenario_pequeno = [
        Entrega(cidades["Natal"], 500, 2),
        Entrega(cidades["Goiania"], 800, 1),
        Entrega(cidades["Rio de Janeiro"], 1200, 2),
    ]

    entregas_cenario_grande = [
        Entrega(cidades["Manaus"], 100, 5),
        Entrega(cidades["Porto Alegre"], 1500, 3),
        Entrega(cidades["Curitiba"], 900, 2),
        Entrega(cidades["Salvador"], 800, 2),
        Entrega(cidades["Joao Pessoa"], 500, 1),
        Entrega(cidades["Belo Horizonte"], 950, 2),
        Entrega(cidades["Campo Grande"], 750, 3),
        Entrega(cidades["Sao Paulo"], 1000, 1),
        Entrega(cidades["Goiania"], 1500, 1),
    ]
    
    return {
        "cenario_pequeno": entregas_cenario_pequeno,
        "cenario_grande": entregas_cenario_grande
    }