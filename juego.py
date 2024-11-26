import random
import rankings


def verificar_estado_juego(vidas: int) -> bool:
    """Devuelve False si `vidas` es igual a 0 y True si `vidas` es mayor a 0"""              
    if vidas > 0:
        return True
    else:
        return False

def ingresar_numero(minimo: int, maximo: int) -> int:
    """Verifica si el numero ingresado esta dentro del rango permitido entre `minimo` y `maximo`"""
    while True:
        try:
            numero = int(input(f"Ingrese un número entre {minimo} y {maximo}: "))
            if minimo <= numero <= maximo:
                return numero
            else:
                print("Número fuera de rango, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida, por favor ingresa un número entero.")

def modificar_vidas(vidas: int, cambio: int) -> int:
    """Devuelve la suma entre `vidas` y `cambio` para ser utilizado en la funcion `jugar_juego`"""
    return vidas + cambio

def generar_respuesta_aleatoria(minimo: int, maximo: int) -> int:
    """Utiliza la libreria random para generar un numero aleatorio en un rango de dos numeros"""
    return random.randint(minimo, maximo)

def jugar_juego(jugador: str):
    """Controla el flujo principal del juego, permitiendo que el jugador intente adivinar
    un número secreto entre 1 y 100. El jugador tiene 6 vidas y el puntaje se actualiza 
    tras cada intento fallido. Al final, se utilizan funciones de rankings.py que guardan
    la puntuacion."""
    vidas = 6
    puntaje = vidas * 10
    numero_secreto = generar_respuesta_aleatoria(1, 100)

    while verificar_estado_juego(vidas):  
        print(f"\nTienes {vidas} vidas y {puntaje} puntos.")
        adivinanza = ingresar_numero(1, 100)  

        if adivinanza < numero_secreto:
            print("Demasiado bajo.")
            vidas = modificar_vidas(vidas, -1)
            puntaje = vidas * 10
        elif adivinanza > numero_secreto:
            print("Demasiado alto.")
            vidas = modificar_vidas(vidas, -1)
            puntaje = vidas * 10
        else:
            print(f"\n¡Felicidades! Adivinaste el número {numero_secreto}.")
            break

    if vidas == 0:
        print(f"\nGame Over! El numero secreto era {numero_secreto}.")

    rankings.guardar_puntuacion(jugador, puntaje)
    rankings.mostrar_rankings()
