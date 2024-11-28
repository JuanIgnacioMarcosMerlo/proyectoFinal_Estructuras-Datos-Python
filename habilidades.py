from grafos import Grafo

class Grafo:
    def __init__(self):
        self.adyacencias = {}
    def agregar_habilidad(self, habilidad):
        if habilidad not in self.adyacencias:
            self.adyacencias[habilidad] = []
    def agregar_dependencia(self, habilidad, prerequisito):
        if habilidad in self.adyacencias:
            self.adyacencias[habilidad].append(prerequisito)
        else:
            self.adyacencias[habilidad] = [prerequisito]
    def dfs_topologico(self, habilidad, visitado, pila):
        visitado.add(habilidad) 
        for prerequisito in self.adyacencias.get(habilidad, []):
            if prerequisito not in visitado:
                self.dfs_topologico(prerequisito, visitado, pila)
        pila.insert(0, habilidad)
    def ordenamiento_topologico(self):
        visitado = set()
        pila = []
        for habilidad in self.adyacencias:
            if habilidad not in visitado:
                self.dfs_topologico(habilidad, visitado, pila)
        return pila

entrenamiento_personaje = Grafo()
entrenamiento_personaje.agregar_habilidad("Control de energía")
entrenamiento_personaje.agregar_habilidad("Control de ki")
entrenamiento_personaje.agregar_habilidad("Levitar")
entrenamiento_personaje.agregar_habilidad("Vuelo")
entrenamiento_personaje.agregar_habilidad("Kamehameha")
entrenamiento_personaje.agregar_habilidad("Genkidama")
entrenamiento_personaje.agregar_dependencia("Genkidama", "Kamehameha")
entrenamiento_personaje.agregar_dependencia("Kamehameha", "Control de ki")
entrenamiento_personaje.agregar_dependencia("Vuelo", "Levitar")
entrenamiento_personaje.agregar_dependencia("Levitar", "Control de energía")
orden_entrenamiento = entrenamiento_personaje.ordenamiento_topologico()
print("Orden de entrenamiento para el personaje:")
for habilidad in reversed(orden_entrenamiento): 
    print(habilidad)

class Personaje:
    def __init__(self):
        self.habilidades_aprendidas = set()
        self.esferas = set()
        self.en_ssj = False 

    def aprender_habilidad(self, habilidad):
        self.habilidades_aprendidas.add(habilidad)

    def agregar_esfera(self, esfera):
        self.esferas.add(esfera)

    def verificar_transformacion(self):
        tiene_genkidama = "Genkidama" in self.habilidades_aprendidas
        tiene_todas_las_esferas = len(self.esferas) >= 7
        if tiene_genkidama and tiene_todas_las_esferas:
            self.en_ssj = True
            print("¡El personaje se ha transformado en Super Saiyan (SSJ)!")
        else:
            self.en_ssj = False
            print("El personaje no puede transformarse en Super Saiyan (SSJ).")
