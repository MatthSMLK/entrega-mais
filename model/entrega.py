# model/entrega.py

class Entrega:
    """
    Representa uma entrega com destino, peso e prazo máximo.
    """
    def __init__(self, destino, peso, prazo_dias):
        self.destino = destino  # Cidade (objeto)
        self.peso = peso        # Em kg
        self.prazo_dias = prazo_dias
