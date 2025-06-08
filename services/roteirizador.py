# services/roteirizador.py

from models.caminhao import Caminhao

class Roteirizador:
    """
    Classe que agora recebe uma instância de qualquer implementação de Grafo.
    """
    def __init__(self, grafo, centros_distribuicao_nomes, num_caminhoes_por_cd=3):
        self.grafo = grafo
        self.centros_distribuicao = centros_distribuicao_nomes
        self.frotas_por_cd = {
            cd_nome: [Caminhao() for _ in range(num_caminhoes_por_cd)]
            for cd_nome in self.centros_distribuicao
        }
        self.cache_dijkstra = {}
        # print(f"Frotas configuradas: { {cd: len(frota) for cd, frota in self.frotas_por_cd.items()} } caminhões por CD.")

    def _executar_dijkstra_cache(self, origem, use_heap):
        """Executa Dijkstra (com ou sem heap) e armazena o resultado em cache."""
        cache_key = (origem, use_heap)
        if cache_key not in self.cache_dijkstra:
            self.cache_dijkstra[cache_key] = self.grafo.dijkstra(origem, use_heap)
        return self.cache_dijkstra[cache_key]

    def encontrar_cd_mais_proximo(self, destino_nome, use_heap):
        """
        Encontra o CD mais próximo usando a implementação de grafo fornecida.
        """
        menor_distancia = float('infinity')
        cd_mais_proximo = None
        melhor_caminho = []

        for cd_nome in self.centros_distribuicao:
            distancias, predecessores = self._executar_dijkstra_cache(cd_nome, use_heap)
            distancia_atual = distancias.get(destino_nome, float('infinity'))

            if distancia_atual < menor_distancia:
                menor_distancia = distancia_atual
                cd_mais_proximo = cd_nome
                # Obter caminho usando o método do grafo
                destino_idx = self.grafo.node_map.get(destino_nome)
                # O predecessor dict agora usa nomes como chaves
                caminho_nomes = []
                curr = destino_nome
                while curr is not None:
                    caminho_nomes.append(curr)
                    curr = predecessores[curr]
                melhor_caminho = caminho_nomes[::-1]

        return cd_mais_proximo, menor_distancia, melhor_caminho

    def processar_entregas(self, entregas, use_heap=True):
        """
        Processa uma lista de entregas, agora com a opção de usar heap no Dijkstra.
        """
        entregas_alocadas = 0
        entregas_nao_alocadas = []
        log_resultados = []

        for frota in self.frotas_por_cd.values():
            for caminhao in frota:
                caminhao.resetar_dia()
        self.cache_dijkstra.clear()

        for entrega in entregas:
            destino_nome = entrega.destino.nome
            cd_partida, distancia_km, caminho = self.encontrar_cd_mais_proximo(destino_nome, use_heap)

            if cd_partida is None:
                entregas_nao_alocadas.append(entrega)
                continue

            tempo_estimado_horas = distancia_km / 60.0
            
            caminhao_alocado = None
            for caminhao in self.frotas_por_cd[cd_partida]:
                if caminhao.pode_transportar(entrega.peso, tempo_estimado_horas):
                    caminhao.alocar_entrega(entrega.peso, tempo_estimado_horas)
                    caminhao_alocado = caminhao
                    break

            if caminhao_alocado:
                entregas_alocadas += 1
                prazo_ok = (tempo_estimado_horas / 24.0) <= entrega.prazo_dias
                log_resultados.append({
                    "Destino": destino_nome, "Alocado": "Sim", "CD Partida": cd_partida,
                    "Distancia (km)": distancia_km, "Tempo (h)": tempo_estimado_horas,
                    "Caminho": ' -> '.join(caminho), "Prazo OK": prazo_ok
                })
            else:
                entregas_nao_alocadas.append(entrega)
                log_resultados.append({
                    "Destino": destino_nome, "Alocado": "Não", "CD Partida": cd_partida,
                    "Distancia (km)": distancia_km, "Tempo (h)": tempo_estimado_horas,
                    "Caminho": ' -> '.join(caminho), "Prazo OK": False
                })

        return log_resultados, entregas_alocadas, entregas_nao_alocadas