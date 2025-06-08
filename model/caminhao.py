# model/caminhao.py

class Caminhao:
    """
    Representa um caminhão com capacidade máxima de carga e limite diário de horas de operação.
    Cada caminhão mantém o controle de sua carga atual e horas usadas em um dia de operação
    para respeitar as restrições de capacidade e tempo de viagem.
    """
    def __init__(self, capacidade_kg=2000, limite_horas=8):
        # Capacidade máxima de carga em kg
        self.capacidade_kg = capacidade_kg
        # Limite de horas de operação diária
        self.limite_horas = limite_horas
        # Carga atual do caminhão em kg
        self.carga_atual = 0
        # Horas já utilizadas pelo caminhão no dia
        self.horas_usadas = 0

    def pode_transportar(self, peso, tempo_estimado):
        """
        Verifica se o caminhão pode realizar uma nova entrega com o peso e tempo fornecidos,
        respeitando sua capacidade restante e limite de horas.
        """
        # Verifica se adicionar o novo peso não excede a capacidade total do caminhão
        # E se o tempo estimado para a entrega não excede o limite diário de horas do caminhão.
        return (
            self.carga_atual + peso <= self.capacidade_kg and
            self.horas_usadas + tempo_estimado <= self.limite_horas
        )

    def alocar_entrega(self, peso, tempo_estimado):
        """
        Atualiza o estado do caminhão, adicionando o peso da entrega à sua carga atual
        e o tempo estimado de viagem às horas já usadas.
        Este método deve ser chamado apenas se 'pode_transportar' retornar True.
        """
        self.carga_atual += peso
        self.horas_usadas += tempo_estimado

    def resetar_dia(self):
        """
        Reseta a carga e as horas usadas do caminhão para um novo dia de operação.
        Isso simula o caminhão estando pronto para novas entregas.
        """
        self.carga_atual = 0
        self.horas_usadas = 0