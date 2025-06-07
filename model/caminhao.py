# model/caminhao.py

class Caminhao:
    """
    Representa um caminhão com capacidade máxima e limite diário de horas.
    """
    def __init__(self, capacidade_kg=2000, limite_horas=8):
        self.capacidade_kg = capacidade_kg
        self.limite_horas = limite_horas
        self.carga_atual = 0
        self.horas_usadas = 0

    def pode_transportar(self, peso, tempo_estimado):
        """
        Verifica se o caminhão pode realizar uma entrega com o peso e tempo fornecidos.
        """
        return (
            self.carga_atual + peso <= self.capacidade_kg and
            self.horas_usadas + tempo_estimado <= self.limite_horas
        )

    def alocar_entrega(self, peso, tempo_estimado):
        """
        Atualiza o estado do caminhão com a entrega alocada.
        """
        self.carga_atual += peso
        self.horas_usadas += tempo_estimado
