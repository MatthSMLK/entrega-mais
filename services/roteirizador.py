# services/roteirizador.py

from models.caminhao import Caminhao

class Roteirizador:
    """
    Classe refatorada para usar um Grafo na otimização de rotas.
    """
    def __init__(self, grafo, centros_distribuicao_nomes, num_caminhoes_por_cd=3):
        self.grafo = grafo
        self.centros_distribuicao = centros_distribuicao_nomes
        self.frotas_por_cd = {
            cd_nome: [Caminhao() for _ in range(num_caminhoes_por_cd)]
            for cd_nome in self.centros_distribuicao
        }
        # Cache para armazenar os resultados de Dijkstra e evitar recálculos
        self.cache_dijkstra = {}
        print(f"Frotas configuradas: { {cd: len(frota) for cd, frota in self.frotas_por_cd.items()} } caminhões por CD.")

    def _executar_dijkstra_cache(self, origem):
        """Executa Dijkstra e armazena o resultado em cache."""
        if origem not in self.cache_dijkstra:
            self.cache_dijkstra[origem] = self.grafo.dijkstra(origem)
        return self.cache_dijkstra[origem]

    def encontrar_cd_mais_proximo(self, destino_nome):
        """
        Encontra o CD mais próximo de um destino usando as distâncias reais do grafo
        calculadas pelo algoritmo de Dijkstra.
        """
        menor_distancia = float('infinity')
        cd_mais_proximo = None
        melhor_caminho = []

        for cd_nome in self.centros_distribuicao:
            distancias, predecessores = self._executar_dijkstra_cache(cd_nome)
            distancia_atual = distancias.get(destino_nome, float('infinity'))

            if distancia_atual < menor_distancia:
                menor_distancia = distancia_atual
                cd_mais_proximo = cd_nome
                melhor_caminho = self.grafo.obter_caminho(predecessores, destino_nome)
        
        return cd_mais_proximo, menor_distancia, melhor_caminho

    def processar_entregas(self, entregas):
        """
        Processa uma lista de entregas, alocando-as a caminhões com base nas rotas
        otimizadas pelo grafo.
        """
        print(f"\n--- Processando {len(entregas)} Entregas ---")
        entregas_alocadas = 0
        entregas_nao_alocadas = []

        # Reseta os caminhões para um novo dia de simulação
        for frota in self.frotas_por_cd.values():
            for caminhao in frota:
                caminhao.resetar_dia()
        self.cache_dijkstra.clear() # Limpa o cache para cada novo processamento

        for i, entrega in enumerate(entregas):
            destino_nome = entrega.destino.nome
            print(f"\n[{i+1}/{len(entregas)}] Processando entrega para {destino_nome} (Peso: {entrega.peso}kg, Prazo: {entrega.prazo_dias} dias)...")

            cd_partida, distancia_km, caminho = self.encontrar_cd_mais_proximo(destino_nome)

            if cd_partida is None:
                print(f"   ❌ Erro: Não foi encontrada uma rota para {destino_nome}.")
                entregas_nao_alocadas.append(entrega)
                continue

            # Simula uma velocidade média de 60 km/h para calcular o tempo
            tempo_estimado_horas = distancia_km / 60.0
            
            # Tenta alocar a entrega a um caminhão
            caminhao_alocado = None
            for caminhao in self.frotas_por_cd[cd_partida]:
                if caminhao.pode_transportar(entrega.peso, tempo_estimado_horas):
                    caminhao.alocar_entrega(entrega.peso, tempo_estimado_horas)
                    caminhao_alocado = caminhao
                    break

            if caminhao_alocado:
                entregas_alocadas += 1
                prazo_ok = (tempo_estimado_horas / 24.0) <= entrega.prazo_dias
                status_prazo = "✅ Dentro do prazo" if prazo_ok else "❌ Fora do prazo"

                print(f"   - ✅ Alocado! Rota saindo de {cd_partida}.")
                print(f"   - Rota: {' -> '.join(caminho)}")
                print(f"   - Distância: {distancia_km:.2f} km")
                print(f"   - Tempo Estimado: {tempo_estimado_horas:.2f} h")
                print(f"   - Status do Prazo: {status_prazo}")
                print(f"   - Caminhão ID ({id(caminhao_alocado) % 1000}): Carga {caminhao_alocado.carga_atual}kg, Horas {caminhao_alocado.horas_usadas:.2f}h")
            else:
                entregas_nao_alocadas.append(entrega)
                print(f"   - ❌ Não Alocado: Sem caminhão disponível ou capaz no CD '{cd_partida}'.")

        print("\n--- Resumo Final do Cenário ---")
        print(f"Total de entregas: {len(entregas)}")
        print(f"Alocadas com sucesso: {entregas_alocadas}")
        print(f"Não alocadas: {len(entregas_nao_alocadas)}")
        if entregas_nao_alocadas:
            print("Detalhes das entregas não alocadas:")
            for e in entregas_nao_alocadas:
                print(f"  - {e.destino.nome} ({e.peso}kg, {e.prazo_dias} dias)")