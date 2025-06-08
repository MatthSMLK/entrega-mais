# controller/roteirizador.py

from model.caminhao import Caminhao
from collections import defaultdict # Para organizar frotas por CD

class Roteirizador:
    """
    A classe Roteirizador é responsável por otimizar o processo de roteamento de entregas.
    Ela identifica o centro de distribuição mais próximo para cada entrega,
    calcula as rotas (distâncias e tempos), e tenta alocar caminhões disponíveis
    respeitando suas capacidades e limites de horas.
    """
    def __init__(self, centros_distribuicao, num_caminhoes_por_cd=3):
        self.centros_distribuicao = centros_distribuicao
        # Dicionário para armazenar a frota de caminhões de cada CD.
        # Cada CD terá uma lista de objetos Caminhao.
        self.frotas_por_cd = {
            cd.nome: [Caminhao() for _ in range(num_caminhoes_por_cd)]
            for cd in centros_distribuicao
        }
        print(f"Frotas iniciais configuradas por CD: { {cd_nome: len(frota) for cd_nome, frota in self.frotas_por_cd.items()} } caminhões cada.")

    def centro_mais_proximo(self, destino):
        """
        Determina e retorna o centro de distribuição mais próximo de uma cidade destino.
        Utiliza a distância euclidiana calculada pela classe Cidade.
        """
        # A função `min` com uma chave `lambda` encontra o objeto na lista
        # que minimiza a função de distância.
        return min(self.centros_distribuicao, key=lambda cd: cd.distancia_para(destino))

    def calcular_rota_e_tempo(self, origem, destino):
        """
        Calcula a distância e o tempo estimado para a rota entre uma origem e um destino.
        No contexto deste projeto, a "rota ideal" é a distância euclidiana,
        e o tempo é estimado com base em uma velocidade média.
        Em um cenário mais complexo, o algoritmo de Dijkstra seria invocado aqui
        para encontrar o caminho mais curto em um grafo com pesos de arestas.
        """
        distancia_km = origem.distancia_para(destino)
        # Simulando uma velocidade média de 60 km/h.
        tempo_estimado_horas = distancia_km / 60.0
        return distancia_km, tempo_estimado_horas

    def alocar_caminhao_para_entrega(self, cd_origem, entrega):
        """
        Tenta encontrar e alocar um caminhão disponível no centro de distribuição de origem
        que possa realizar a entrega, respeitando peso e tempo de operação.
        """
        # Calcula a distância e o tempo para esta entrega específica
        distancia_km, tempo_estimado = self.calcular_rota_e_tempo(cd_origem, entrega.destino)

        caminhao_encontrado = None
        # Itera sobre os caminhões disponíveis na frota do CD de origem
        for caminhao in self.frotas_por_cd[cd_origem.nome]:
            # Verifica se o caminhão pode transportar o peso e tem tempo disponível
            if caminhao.pode_transportar(entrega.peso, tempo_estimado):
                # Se puder, aloca a entrega para este caminhão
                caminhao.alocar_entrega(entrega.peso, tempo_estimado)
                caminhao_encontrado = caminhao
                break # Encontrou um caminhão, sai do loop

        return caminhao_encontrado, distancia_km, tempo_estimado

    def processar_entregas(self, entregas):
        """
        Processa uma lista de entregas, tentando alocar cada uma ao centro de distribuição
        mais próximo e a um caminhão disponível, verificando restrições de prazo, peso e tempo.
        """
        print(f"\n--- Processando {len(entregas)} Entregas ---")
        entregas_alocadas_com_sucesso = 0
        entregas_nao_alocadas = []

        # Resetar o estado de todos os caminhões para o início de um novo processamento/dia
        for cd_nome in self.frotas_por_cd:
            for caminhao in self.frotas_por_cd[cd_nome]:
                caminhao.resetar_dia()

        for i, entrega in enumerate(entregas):
            print(f"\n[{i+1}/{len(entregas)}] Processando {entrega.destino.nome} (Peso: {entrega.peso}kg, Prazo: {entrega.prazo_dias} dias)...")
            
            # Encontra o CD mais próximo para esta entrega 
            cd_mais_proximo = self.centro_mais_proximo(entrega.destino)
            
            # Tenta alocar um caminhão e obter os detalhes da rota
            caminhao_alocado, distancia_km, tempo_estimado_horas = \
                self.alocar_caminhao_para_entrega(cd_mais_proximo, entrega)

            status_alocacao = ""
            status_prazo = ""

            # Verifica se a entrega foi alocada a um caminhão
            if caminhao_alocado:
                entregas_alocadas_com_sucesso += 1
                status_alocacao = "✅ Alocado"
                
                # Verifica se o tempo estimado de viagem respeita o prazo em dias 
                # Considerando 24 horas por dia para o prazo.
                if (tempo_estimado_horas / 24.0) <= entrega.prazo_dias:
                    status_prazo = "✅ Dentro do prazo"
                else:
                    status_prazo = "❌ Fora do prazo"
                    print(f"   ATENÇÃO: Tempo estimado ({tempo_estimado_horas:.2f}h) excede o prazo de {entrega.prazo_dias} dias.")
                
                print(f"   - CD de partida: {cd_mais_proximo.nome}")
                print(f"   - Distância: {distancia_km:.2f} km")
                print(f"   - Tempo estimado: {tempo_estimado_horas:.2f} h")
                print(f"   - Caminhão utilizado (ID: {id(caminhao_alocado) % 1000}): Carga {caminhao_alocado.carga_atual}kg/{caminhao_alocado.capacidade_kg}kg, Horas {caminhao_alocado.horas_usadas:.2f}h/{caminhao_alocado.limite_horas}h")
                print(f"   - Status Geral: {status_alocacao}, {status_prazo}")
            else:
                # Se nenhum caminhão pôde ser alocado, a entrega falhou 
                status_alocacao = "❌ Não Alocado (sem caminhão disponível ou capaz)"
                entregas_nao_alocadas.append(entrega)
                print(f"   - Status Geral: {status_alocacao}")


        print(f"\n--- Resumo Final do Cenário ---")
        print(f"Total de entregas no cenário: {len(entregas)}")
        print(f"Entregas alocadas com sucesso: {entregas_alocadas_com_sucesso}")
        print(f"Entregas não alocadas: {len(entregas_nao_alocadas)}")
        if entregas_nao_alocadas:
            print("Detalhes das entregas não alocadas:")
            for entrega in entregas_nao_alocadas:
                print(f"  - {entrega.destino.nome} (Peso: {entrega.peso}kg, Prazo: {entrega.prazo_dias} dias)")