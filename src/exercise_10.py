def calcular_puntaje_ronda(scores_dict):
    """Suma los puntos de los jueces para cada participante."""
    return {nombre: sum(jueces.values()) for nombre, jueces in scores_dict.items()}


def obtener_ganador(resultados_ronda):
    """Encuentra el puntaje más alto de la ronda actual."""
    return max(resultados_ronda, key=resultados_ronda.get)


def imprimir_tabla(titulo, data_lista, es_final=False):
    """Imprime una tabla."""
    print(f"\n--- {titulo} ---\n")
    if not es_final:
        print(f"{'Cocinero':<10} | {'Puntos'}\n")
        for nombre, puntos in data_lista.items():
            print(f"{nombre:<10} | {puntos}")
    else:
        print(
            f"{'Cocinero':<10} | {'Total':<5} | {'Ganadas':<7} | {'Mejor':<5} | {'Promedio'}"
        )
        print("-" * 50)
        for c in data_lista:
            print(
                f"{c['name']:<10} | {c['total']:<5} | {c['wins']:<7} | {c['best']:<5} | {c['avg']:.1f}"
            )
        print("-" * 50)
