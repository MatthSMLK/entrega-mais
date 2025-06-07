# controller/roteirizador.py

from model.caminhao import Caminhao

def centro_mais_proximo(destino, centros):
    """
    Retorna o centro de distribuição mais próximo de uma cidade destino.
    """
    return min(centros, key=lambda cd: cd.distancia_para(destino))

def processar_entregas(entregas, centros):
    """
    Aloca entregas para o centro mais próximo e verifica se um caminhão pode fazer a entrega.
    """
    for entrega in entregas:
        cd_mais_proximo = centro_mais_proximo(entrega.destino, centros)
        distancia_km = cd_mais_proximo.distancia_para(entrega.destino)
        tempo_estimado = distancia_km / 60 * 1  # Simulando média de 60km/h

        caminhao = Caminhao()
        pode_entregar = caminhao.pode_transportar(entrega.peso, tempo_estimado)

        print(f"\nEntrega para: {entrega.destino.nome}")
        print(f"- CD mais próximo: {cd_mais_proximo.nome}")
        print(f"- Distância estimada: {distancia_km:.2f} km")
        print(f"- Tempo estimado: {tempo_estimado:.2f} h")
        print(f"- Peso: {entrega.peso} kg")
        print(f"- Status: {'✅ Ok' if pode_entregar else '❌ Excede capacidade/tempo'}")
