from personajes import Personaje
from arbolBinario_personajes import ArbolPersonajes
from colaPrioridad import ColaDePrioridad
from grafos import Grafo
from busqueda import dfs, bfs

def crear_personaje(arbol_personajes, cola_prioridad):
    print("=== Crear un nuevo personaje ===")
    nombre = input("Nombre del personaje: ").strip().capitalize()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del personaje: ").strip().capitalize()

    try:
        nivel_poder = int(input("Nivel de poder inicial: "))
        if nivel_poder < 0:
            raise ValueError
    except ValueError:
        print("El nivel de poder debe ser un número positivo. Asignando 0 por defecto.")
        nivel_poder = 0

    print(f"Opciones de raza: {Personaje.RAZAS_VALIDAS}")
    raza = input("Selecciona una raza: ").strip().lower()
    if raza not in Personaje.RAZAS_VALIDAS:
        print("Raza no válida. Se asignará 'Terrícola' por defecto.")
        raza = "terrícola"

    habilidades = input("Introduce habilidades iniciales separadas por comas (o deja en blanco): ")
    habilidades = [h.strip().capitalize() for h in habilidades.split(",") if h.strip()] if habilidades else []

    try:
        poder_ataque = int(input("Poder de ataque: "))
        if poder_ataque < 0 or poder_ataque > 100:
            raise ValueError
    except ValueError:
        print("El poder de ataque debe ser un número entre 0 y 100. Asignando 10 por defecto.")
        poder_ataque = 10

    personaje = Personaje(
        nombre=nombre,
        nivel_poder=nivel_poder,
        habilidades=habilidades,
        raza=raza,
        salud=100,
        poder_ataque=poder_ataque
    )
    arbol_personajes.insertar(personaje)
    print(f"Personaje '{personaje.nombre}' añadido al árbol.")
    cola_prioridad.agregar_a_cola(personaje)
    print(f"Personaje '{personaje.nombre}' añadido a la cola de prioridad.")

    return personaje

def agregar_transformaciones_personaje(personaje):
    while True:
        print("\n=== Gestión de Transformaciones ===")
        print("1. Agregar transformación")
        print("2. Listar transformaciones")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre de la transformación: ").strip()
            
            # Verificar si la transformación ya está agregada
            transformaciones_existentes = [t.split(" (")[0] for t in personaje.transformaciones.listar_transformaciones()]
            if nombre.lower() in [t.lower() for t in transformaciones_existentes]:
                print(f"La transformación '{nombre}' ya está agregada.")
            else:
                try:
                    multiplicador = float(input("Multiplicador de poder: ").strip())
                    personaje.agregar_transformacion(nombre, multiplicador)
                    print(f"Transformación '{nombre}' agregada.")
                except ValueError:
                    print("El multiplicador debe ser un número válido.")
                
        elif opcion == "2":
            transformaciones = personaje.transformaciones.listar_transformaciones()
            if transformaciones:
                print("Transformaciones disponibles:")
                for t in transformaciones:
                    print(f"- {t}")
            else:
                print("No hay transformaciones disponibles.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


def menu_principal(arbol_personajes, cola_prioridad):
    while True:
        print("\n=== Menú Principal ===")
        print("1. Crear personaje")
        print("2. Listar personajes")
        print("3. Ver/editar habilidades de un personaje")
        print("4. Realizar combate")
        print("5. Torneo")
        print("6. Gestión de transformaciones")
        print("7. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_personaje(arbol_personajes, cola_prioridad)

        elif opcion == "2":
            print("\n=== Personajes en el Árbol ===")
            personajes = arbol_personajes.recorrer_inorden()
            if not personajes:
                print("No hay personajes disponibles.")
            else:
                for i, personaje in enumerate(personajes, 1):
                    print(f"{i}. {personaje}")

        elif opcion == "3":
            print("\n=== Gestión de Habilidades ===")
            personajes = arbol_personajes.recorrer_inorden()
            if not personajes:
                print("No hay personajes disponibles.")
                continue
            for i, personaje in enumerate(personajes, 1):
                print(f"{i}. {personaje.nombre}")
            try:
                eleccion = int(input("Elige un personaje (número): ").strip()) - 1
                if 0 <= eleccion < len(personajes):
                    personaje = personajes[eleccion]
                    menu_habilidades(personaje)
                else:
                    print("Número no válido.")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.")

        elif opcion == "4":
            print("\n=== Combate ===")
            personajes = arbol_personajes.recorrer_inorden()
            if len(personajes) < 2:
                print("No hay suficientes personajes para un combate.")
                continue
            print("Selecciona los dos personajes para el combate:")
            for i, personaje in enumerate(personajes, 1):
                print(f"{i}. {personaje.nombre} (Nivel de Poder: {personaje.nivel_poder})")
            try:
                p1 = int(input("Elige el primer personaje (número): ").strip()) - 1
                p2 = int(input("Elige el segundo personaje (número): ").strip()) - 1
                if 0 <= p1 < len(personajes) and 0 <= p2 < len(personajes) and p1 != p2:
                    combate(personajes[p1], personajes[p2])
                else:
                    print("Selección no válida.")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.")

        elif opcion == "5":
            torneo(cola_prioridad)

        elif opcion == "6":
            print("\n=== Gestión de Transformaciones ===")
            personajes = arbol_personajes.recorrer_inorden()
            if not personajes:
                print("No hay personajes disponibles.")
                continue
            for i, personaje in enumerate(personajes, 1):
                print(f"{i}. {personaje.nombre}")
            try:
                eleccion = int(input("Elige un personaje (número): ").strip()) - 1
                if 0 <= eleccion < len(personajes):
                    personaje = personajes[eleccion]
                    if not personaje.transformaciones.listar_transformaciones():
                        print(f"{personaje.nombre} no tiene transformaciones disponibles.")
                        agregar = input("¿Quieres agregar una transformación? (s/n): ").strip().lower()
                        if agregar == "s":
                            agregar_transformaciones_personaje(personaje)
                    else:
                        print(f"Transformaciones disponibles para {personaje.nombre}:")
                        for t in personaje.transformaciones.listar_transformaciones():
                            print(f"- {t}")
                else:
                    print("Número no válido.")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.")

        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo nuevamente.")

def combate(personaje1, personaje2):
    print("\n=== Combate ===")
    print(f"{personaje1.nombre} vs {personaje2.nombre}")

    def gestionar_transformaciones(personaje):
        print(f"\nTransformaciones disponibles para {personaje.nombre}:")
        transformaciones = personaje.transformaciones.listar_transformaciones()
        if transformaciones:
            print("\n".join([f"- {t}" for t in transformaciones]))
        else:
            print(f"{personaje.nombre} no tiene transformaciones disponibles.")
        while True:
            transformarse = input("¿Quieres transformarte o agregar una nueva transformación? (transformar/agregar/ninguna): ").strip().lower()
            if transformarse == "transformar":
                transformacion = input("Elige una transformación: ").strip().lower()
                personaje.aplicar_transformacion(transformacion)
                break
            elif transformarse == "agregar":
                agregar_transformaciones_personaje(personaje)
                print("Transformaciones actualizadas:")
                transformaciones = personaje.transformaciones.listar_transformaciones()
                print("\n".join([f"- {t}" for t in transformaciones]))
            elif transformarse == "ninguna":
                break
            else:
                print("Opción no válida. Inténtalo nuevamente.")

    gestionar_transformaciones(personaje1)
    gestionar_transformaciones(personaje2)


    if personaje1.nivel_poder > personaje2.nivel_poder:
        print(f"\n{personaje1.nombre} gana el combate!")
        personaje1.restaurar_estado_base()
        personaje1.subir_nivel()
    elif personaje1.nivel_poder < personaje2.nivel_poder:
        print(f"\n{personaje2.nombre} gana el combate!")
        personaje2.restaurar_estado_base()
        personaje2.subir_nivel()
    else:
        print("\nEmpate!")
        personaje1.restaurar_estado_base()
        personaje2.restaurar_estado_base()
    while True:
        continuar = input("¿Deseas seguir combatiendo? (s/n): ").strip().lower()
        if continuar == "s":
            personaje2 = crear_personaje(arbol_personajes)
            combate(personaje1, personaje2)
            break
        elif continuar == "n":
            print("Saliendo del combate.")
            print(personaje1)
            break
        else:
            print("Respuesta no válida. Por favor, ingresa 's' o 'n'.")

def menu_habilidades(personaje):
    if personaje.arbol_habilidades is None:
        raiz = input(f"Introduce la habilidad raíz para {personaje.nombre}: ").strip()
        personaje.inicializar_arbol_habilidades(raiz)

    while True:
        print(f"\n=== Menú de Habilidades: {personaje.nombre} ===")
        print("1. Listar habilidades")
        print("2. Agregar mejora")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            personaje.arbol_habilidades.listar_habilidades()

        elif opcion == "2":
            padre = input("Introduce la habilidad padre existente: ").strip()
            nueva_habilidad = input("Introduce la nueva habilidad/mejora: ").strip()
            personaje.arbol_habilidades.agregar_habilidad(padre, nueva_habilidad)

        elif opcion == "3":
            print(f"Saliendo del menú de habilidades para {personaje.nombre}.")
            break

        else:
            print("Opción no válida. Inténtalo nuevamente.")


def torneo(cola_prioridad):
    print("\n=== Torneo de Personajes ===")

    if cola_prioridad.esta_vacia():
        print("No hay personajes en la cola.")
        return

    while len(cola_prioridad.cola) > 1:
        print("\n--- Nuevo Enfrentamiento ---")
        personaje1 = cola_prioridad.extraer_de_cola()
        personaje2 = cola_prioridad.extraer_de_cola()

        print(f"{personaje1.nombre} (Nivel de Poder: {personaje1.nivel_poder}) vs "
              f"{personaje2.nombre} (Nivel de Poder: {personaje2.nivel_poder})")
        if personaje1.nivel_poder > personaje2.nivel_poder:
            print(f"\n{personaje1.nombre} gana el combate!")
            personaje1.restaurar_estado_base()
            personaje1.subir_nivel()
            cola_prioridad.agregar_a_cola(personaje1)
        elif personaje2.nivel_poder > personaje1.nivel_poder:
            print(f"\n{personaje2.nombre} gana el combate!")
            personaje2.restaurar_estado_base()
            personaje2.subir_nivel()
            cola_prioridad.agregar_a_cola(personaje2)
        else:
            print("\nEmpate!")
            cola_prioridad.agregar_a_cola(personaje1)
            cola_prioridad.agregar_a_cola(personaje2)
    ganador = cola_prioridad.extraer_de_cola()
    print(f"\n=== El ganador del torneo es {ganador.nombre}! (Nivel de Poder: {ganador.nivel_poder}) ===")







arbol_personajes = ArbolPersonajes()
cola_prioridad = ColaDePrioridad()
menu_principal(arbol_personajes, cola_prioridad)
universo_dragon_ball = Grafo()
universo_dragon_ball.agregar_planeta("Tierra", enemigo="Raditz", poder=1200, esferas=[4, 5])
universo_dragon_ball.agregar_planeta("Namek", enemigo="Freezer", poder=530000, esferas=[1])
universo_dragon_ball.agregar_planeta("Vegeta", enemigo="Nappa", poder=4000, esferas=[2, 6])
universo_dragon_ball.agregar_planeta("Kaiosama", enemigo="Bubbles", poder=10, esferas=[3, 7])
universo_dragon_ball.agregar_conexion("Tierra", "Namek", 2)
universo_dragon_ball.agregar_conexion("Tierra", "Kaiosama", 3)
universo_dragon_ball.agregar_conexion("Namek", "Vegeta", 4)
universo_dragon_ball.agregar_conexion("Kaiosama", "Vegeta", 6)
universo_dragon_ball.mostrar_grafo()
camino_dfs = dfs(universo_dragon_ball, "Tierra", "Vegeta")
camino_bfs = bfs(universo_dragon_ball, "Tierra", "Vegeta")
print("\nCamino DFS de Tierra a Vegeta:", camino_dfs)
print("Camino BFS de Tierra a Vegeta:", camino_bfs)