# model/cidade.py

class Cidade:
    """
    Representa uma cidade com coordenadas simuladas (x, y).
    Usado para calcular distâncias entre os centros de distribuição e os destinos de entrega.
    """
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    def distancia_para(self, outra_cidade):
        """
        Calcula a distância euclidiana (distância em linha reta) entre duas cidades
        com base em suas coordenadas. Esta distância é utilizada como a "rota mais curta"
        no modelo simplificado do grafo.
        """
        dx = self.x - outra_cidade.x
        dy = self.y - outra_cidade.y
        return (dx**2 + dy**2) ** 0.5

    def __str__(self):
        """Representação em string da cidade, útil para depuração e exibição."""
        return f"{self.nome} ({self.x}, {self.y})"

    def __repr__(self):
        """Representação para listas e estruturas de dados."""
        return self.__str__()

    def __eq__(self, other):
        """Define a igualdade entre objetos Cidade."""
        return isinstance(other, Cidade) and self.nome == other.nome

    def __hash__(self):
        """Permite que objetos Cidade sejam usados como chaves em dicionários ou sets."""
        return hash(self.nome)