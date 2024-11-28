class NodoHabilidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []      
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

class ArbolHabilidades:
    def __init__(self, habilidad_raiz):
        self.raiz = NodoHabilidad(habilidad_raiz)

    def agregar_habilidad(self, habilidad_padre, nueva_habilidad):
        nodo_padre = self._buscar(self.raiz, habilidad_padre)
        if nodo_padre:
            nodo_padre.agregar_hijo(NodoHabilidad(nueva_habilidad))
            print(f"Habilidad '{nueva_habilidad}' agregada como mejora de '{habilidad_padre}'.")
        else:
            print(f"Habilidad '{habilidad_padre}' no encontrada.")
    

    def _buscar(self, nodo, habilidad):    
        if nodo is None:
            return None
        if nodo.nombre == habilidad:
            return nodo
        for hijo in nodo.hijos:
            resultado = self._buscar(hijo, habilidad)
            if resultado:
                return resultado
        return None
    
    def listar_habilidades(self):
        print("Habilidades del personaje:")
        self._listar_habilidades_recursivo(self.raiz, nivel=0)

    def _listar_habilidades_recursivo(self, nodo, nivel):
        if nodo:
            print("  " * nivel + f"- {nodo.nombre}")
            for hijo in nodo.hijos:
                self._listar_habilidades_recursivo(hijo, nivel + 1)