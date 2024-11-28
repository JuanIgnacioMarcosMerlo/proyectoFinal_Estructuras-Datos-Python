class NodoTransformacion:
    def __init__(self, nombre: str, multiplicador: float):
        self.nombre = nombre
        self.multiplicador = multiplicador
        self.siguiente = None

class ListaEnlazadaTransformaciones:
    def __init__(self):
        self.cabeza = None

    def agregar_transformacion(self, nombre: str, multiplicador: float):
        nuevo_nodo = NodoTransformacion(nombre, multiplicador)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar_transformacion(self, nombre: str) -> NodoTransformacion:
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None

    def listar_transformaciones(self):
        actual = self.cabeza
        transformaciones = []
        while actual:
            transformaciones.append(f"{actual.nombre} (x{actual.multiplicador})")
            actual = actual.siguiente
        return transformaciones
