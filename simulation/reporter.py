# simulation/reporter.py

def imprimir_sumario_comparativo(titulo, resultados):
    """
    Imprime uma tabela formatada com o resumo dos tempos de execução,
    destacando o mais rápido e a diferença percentual dos outros.
    """
    print("\n" + "="*70)
    print(f"  {titulo.upper()}  ")
    print("="*70)
    
    if not resultados:
        print("Nenhum resultado para exibir.")
        return

    # Ordena os resultados pelo tempo total para fácil comparação
    resultados_ordenados = sorted(resultados, key=lambda x: x['total_time'])
    mais_rapido = resultados_ordenados[0]
    
    print(f"{'Configuração':<45} | {'Tempo Total (s)':<15} | {'Diferença'}")
    print("-" * 70)

    # Imprime o mais rápido primeiro
    print(f"{mais_rapido['config']:<45} | {mais_rapido['total_time']:<15.6f} | {'(O mais rápido)'}")

    # Imprime os outros, calculando a diferença percentual
    for res in resultados_ordenados[1:]:
        diferenca_percentual = ((res['total_time'] / mais_rapido['total_time']) - 1) * 100
        diff_str = f"+{diferenca_percentual:.2f}% mais lento"
        print(f"{res['config']:<45} | {res['total_time']:<15.6f} | {diff_str}")
    
    print("=" * 70)