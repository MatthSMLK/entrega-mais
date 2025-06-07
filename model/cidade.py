# model/cidade.py

class Cidade:
    """
    Representa uma cidade com coordenadas simuladas.
    """
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    def distancia_para(self, outra_cidade):
        """
        Calcula a distância euclidiana entre duas cidades.
        """
        dx = self.x - outra_cidade.x
        dy = self.y - outra_cidade.y
        return (dx**2 + dy**2) ** 0.5
