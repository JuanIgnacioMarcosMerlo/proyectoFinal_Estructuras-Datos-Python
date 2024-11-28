class Grafo:
    def __init__(self):
        self.adyacencias = {}  
        self.enemigos = {}     
        self.esferas = {}      
    def agregar_planeta(self, planeta, enemigo=None, poder=None , esferas=None):
        if planeta not in self.adyacencias:
            self.adyacencias[planeta] = [] 
            self.enemigos[planeta] = (enemigo, poder)  
            self.esferas[planeta] = (esferas)
    def agregar_conexion(self, origen, destino, peso):
        """
        Agrega una conexión (arista) entre dos nodos con un peso.
        """
        if origen in self.adyacencias and destino in self.adyacencias:
            self.adyacencias[origen].append((destino, peso))
            self.adyacencias[destino].append((origen, peso))

    def mostrar_grafo(self):
        """Muestra las conexiones de cada nodo y el enemigo en cada planeta."""
        print("Planetas y conexiones:")
        for planeta, conexiones in self.adyacencias.items():
            print(f"{planeta} -> {[(destino, peso) for destino, peso in conexiones]}")
        print("\nEnemigos especiales en cada planeta:")
        for planeta, (enemigo, poder) in self.enemigos.items():
            if enemigo:
                print(f"{planeta}: Enemigo {enemigo} con poder {poder}")
            else:
                print(f"{planeta}: Sin enemigo asignado")      
        for planeta, esferas in self.esferas.items():
            if esferas:
                print(f"{planeta}: Esferas {esferas}")
        else:
            print(f"{planeta}: No hay esfera")




# Crear una instancia del grafo
universo_dragon_ball = Grafo()

# Agregar planetas con enemigos especiales
universo_dragon_ball.agregar_planeta("Tierra", enemigo="Raditz", poder=1200, esferas=[4, 5])
universo_dragon_ball.agregar_planeta("Namek", enemigo="Freezer", poder=530000, esferas=[1])
universo_dragon_ball.agregar_planeta("Vegeta", enemigo="Nappa", poder=4000, esferas=[2,6])
universo_dragon_ball.agregar_planeta("Kaiosama", enemigo="Bubbles", poder=10, esferas=[3,7])

# Agregar conexiones entre planetas
universo_dragon_ball.agregar_conexion("Tierra", "Namek", 2)
universo_dragon_ball.agregar_conexion("Tierra", "Kaiosama", 3)
universo_dragon_ball.agregar_conexion("Namek", "Vegeta", 4)
universo_dragon_ball.agregar_conexion("Kaiosama", "Vegeta", 6)

# Mostrar el grafo con enemigos especiales
universo_dragon_ball.mostrar_grafo()
