# models/cidade.py

class Cidade:
    """
    Representa uma cidade (ou local) no sistema.
    Agora é uma estrutura de dados mais simples, contendo apenas o nome.
    O cálculo de distância foi movido para a classe Grafo.
    """
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome