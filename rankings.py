ranking = {}

def agregar_dato(jugador: str, puntaje: int):
    """Agrega el nombre del jugador y su puntaje al diccionario `ranking`"""
    ranking[jugador] = puntaje

def ordenar_puntuaciones() -> dict:
    """Se utiliza el metodo `sort` para ordenar las puntuaciones de los jugadores de manera descendente"""
    puntuaciones = list(ranking.items())  
    # Función para extraer el puntaje
    def obtener_puntaje(item):
        return item[1]
    # Ordenar usando sort()
    puntuaciones.sort(key=obtener_puntaje, reverse=True)
    return dict(puntuaciones)

def guardar_puntuacion(jugador: str, puntaje: int):
    """Se guardan el nombre del jugador y su puntaje en el archivo ranking.txt"""
    agregar_dato(jugador, puntaje)
    with open("ranking.txt", mode="a") as file:
        file.write(f"{jugador}, {puntaje}\n")

def mostrar_rankings() -> str:
    """Imprime por pantalla los nombres y puntajes de los jugadores"""
    print("Ranking de jugadores:")
    for jugador, puntaje in ordenar_puntuaciones().items():
        print(f"{jugador}: {puntaje}")
