# data/distancias.py

from model.cidade import Cidade

# Define cidades com coordenadas simuladas
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
}

centros_distribuicao = [
    cidades["Belem"],
    cidades["Recife"],
    cidades["Brasilia"],
    cidades["Sao Paulo"],
    cidades["Florianopolis"],
]
