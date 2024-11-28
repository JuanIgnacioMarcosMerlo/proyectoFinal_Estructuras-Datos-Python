from arbolHabilidades import ArbolHabilidades
from listaTranformaciones import ListaEnlazadaTransformaciones

class Personaje:
    RAZAS_VALIDAS = ["saiyajin", "namekuseijin", "terrícola", "androide", "freezer race"]
    
    def __init__(self, nombre, nivel_poder, nivel=0, habilidades=None, raza="terrícola", salud=100, poder_ataque=10):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if nivel_poder < 0:
            raise ValueError("El nivel de poder debe ser un número positivo.")
        if raza not in Personaje.RAZAS_VALIDAS:
            raise ValueError(f"La raza '{raza}' no es válida. Opciones: {Personaje.RAZAS_VALIDAS}")
        if habilidades is None:
            habilidades = []
        elif not isinstance(habilidades, list):
            raise ValueError("Las habilidades deben ser una lista.")
        if salud <= 0:
            raise ValueError("La salud debe ser un número positivo.")
        if poder_ataque <= 0:
            raise ValueError("El poder de ataque debe ser un número positivo.")
        if nivel < 0:
            raise ValueError("El nivel debe ser un número positivo.")

        self.nombre = nombre
        self.nivel_poder = nivel_poder
        self.nivel = nivel
        self.habilidades = habilidades
        self.raza = raza
        self.salud = salud
        self.poder_ataque = poder_ataque
        self.estado_base = {
            "nivel_poder": nivel_poder,
            "salud": salud,
            "poder_ataque": poder_ataque
        }
        self.arbol_habilidades = None
        self.transformaciones = ListaEnlazadaTransformaciones()

    def agregar_transformacion(self, nombre, multiplicador):
        self.transformaciones.agregar_transformacion(nombre, multiplicador)

    def aplicar_transformacion(self, transformacion):
        nodo = self.transformaciones.buscar_transformacion(transformacion)
        if nodo:
            self.nivel_poder *= nodo.multiplicador
            self.salud *= nodo.multiplicador
            self.poder_ataque *= nodo.multiplicador
            print(f"{self.nombre} se transformó en {transformacion} y ahora tiene un nivel de poder de {self.nivel_poder}.")
        else:
            print(f"La transformación '{transformacion}' no está disponible para {self.nombre}.")


    def restaurar_estado_base(self):
        self.nivel_poder = self.estado_base["nivel_poder"]
        self.salud = self.estado_base["salud"]
        self.poder_ataque = self.estado_base["poder_ataque"]

    def subir_nivel(self):
        self.nivel += 1
        self.nivel_poder += 1000
        self.salud += 50
        self.poder_ataque += 10
        print(f"{self.nombre} subió de nivel! Nivel actual: {self.nivel}")


    def inicializar_arbol_habilidades(self, habilidad_raiz):
        self.arbol_habilidades = ArbolHabilidades(habilidad_raiz)
        print(f"Árbol de habilidades inicializado con la raíz: '{habilidad_raiz}'.")

   

    def __str__(self):
        return (f"Personaje: {self.nombre} | Raza: {self.raza.capitalize()} | "
                f"Nivel de Poder: {self.nivel_poder} | Habilidades: {', '.join(self.habilidades)} | "
                f"Salud: {self.salud} | Poder de Ataque: {self.poder_ataque} | Nivel: {self.nivel}")