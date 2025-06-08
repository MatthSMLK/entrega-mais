# data/distancias.py

from model.cidade import Cidade

# Define cidades com coordenadas simuladas
# Estas coordenadas são usadas para calcular a distância euclidiana entre cidades,
# simulando um mapa de distâncias para o algoritmo de roteamento.
cidades = {
    "Belem": Cidade("Belem", 0, 0),
    "Recife": Cidade("Recife", 2, 4),
    "Brasilia": Cidade("Brasilia", 5, 2),
    "Sao Paulo": Cidade("Sao Paulo", 8, -1),
    "Florianopolis": Cidade("Florianopolis", 10, -4),
    "Natal": Cidade("Natal", 3, 6),
    "Joao Pessoa": Cidade("Joao Pessoa", 2.5, 5.5),
    "Salvador": Cidade("Salvador", 4, 3),
    "Goiania": Cidade("Goiania", 5, 1),
    "Rio de Janeiro": Cidade("Rio de Janeiro", 7, 0),
    "Curitiba": Cidade("Curitiba", 9, -2),
    "Porto Alegre": Cidade("Porto Alegre", 11, -5),
    # Adicionei mais cidades para maior variedade nos testes
    "Fortaleza": Cidade("Fortaleza", 1.5, 5.5),
    "Belo Horizonte": Cidade("Belo Horizonte", 6.5, 0.5),
    "Manaus": Cidade("Manaus", -3, 3),
    "Campo Grande": Cidade("Campo Grande", 7, -2.5),
}

# Centros de distribuição, conforme especificado no problema.
# A empresa possui cinco centros de distribuição localizados em Belém (PA), Recife (PE),
# Brasília (DF), São Paulo (SP) e Florianópolis (SC).
centros_distribuicao = [
    cidades["Belem"],
    cidades["Recife"],
    cidades["Brasilia"],
    cidades["Sao Paulo"],
    cidades["Florianopolis"],
]