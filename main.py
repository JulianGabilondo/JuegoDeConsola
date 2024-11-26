import rankings
import juego

def ingresar_nombre_usuario() -> str:
    """Verifica que el nombre ingresado no esté dentro del diccionario `ranking`, luego lo retorna"""
    while True:
        try:
            nombre = input("Ingresa tu nombre: ")
            if nombre in rankings.ranking:
                raise ValueError("El nombre ingresado ya existe. Prueba otro nombre")
            return nombre
        except ValueError as e:
            print(e)

nombre_juego = """ADIVINANZAS DE NUMEROS
                        #Naughty Cat"""
cuadro = f"""
+{'-' * (len(nombre_juego) + 2)}+
                    {nombre_juego} 
+{'-' * (len(nombre_juego) + 2)}+
    """

def mostrar_menu() -> str:
    """Imprime por pantalla el menu del juego"""
    print(cuadro)
    print("""
1. Jugar
2. Mostrar Ranking
3. Cambiar Usuario
4. Salir""")

while True:
    nombre_usuario = ingresar_nombre_usuario()
    while True:
        mostrar_menu()
        opcion = juego.ingresar_numero(1, 4)

        if opcion == 1:
            juego.jugar_juego(nombre_usuario)
        elif opcion == 2:
            rankings.mostrar_rankings()
        elif opcion == 3:
            break
        elif opcion == 4:
            print('''

Saliendo del juego...



# Juego creado por Naughty Cat #
''')
            exit()