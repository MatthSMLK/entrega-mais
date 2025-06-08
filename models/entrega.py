# model/entrega.py

class Entrega:
    """
    Representa uma entrega com seu destino, peso e prazo máximo para ser realizada.
    As entregas são associadas aos locais de destino e aos prazos de entrega.
    """
    def __init__(self, destino, peso, prazo_dias):
        self.destino = destino  # Objeto Cidade para o destino da entrega
        self.peso = peso        # Peso da encomenda em kg
        self.prazo_dias = prazo_dias # Prazo máximo em dias para a entrega

    def __str__(self):
        """Representação em string da entrega, útil para depuração e exibição."""
        return f"Entrega para {self.destino.nome} (Peso: {self.peso}kg, Prazo: {self.prazo_dias} dias)"

    def __repr__(self):
        """Representação para listas e estruturas de dados."""
        return self.__str__()