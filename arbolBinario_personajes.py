class Nodo:
    def __init__(self, personaje):
        self.personaje = personaje  
        self.izquierdo = None
        self.derecho = None

class ArbolPersonajes:
    def __init__(self):
        self.raiz = None

    def insertar(self, personaje):
        if not self.raiz:
            self.raiz = Nodo(personaje)
        else:
            self._insertar_recursivo(personaje, self.raiz)

    def _insertar_recursivo(self, personaje, nodo):
        if personaje.nivel_poder < nodo.personaje.nivel_poder:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(personaje)
            else:
                self._insertar_recursivo(personaje, nodo.izquierdo)
        elif personaje.nivel_poder > nodo.personaje.nivel_poder:
            if nodo.derecho is None:
                nodo.derecho = Nodo(personaje)
            else:
                self._insertar_recursivo(personaje, nodo.derecho)
        else:
            raise ValueError("Personaje ya existe en el árbol.")

    def buscar_mas_fuerte(self):
        if not self.raiz:
            return None
        return self._buscar_maximo(self.raiz)

    def _buscar_maximo(self, nodo):
        if nodo.derecho is None:
            return nodo.personaje
        return self._buscar_maximo(nodo.derecho)
    
    def recorrer_inorden(self):
        personajes = []
        self._recorrer_inorden_recursivo(self.raiz, personajes)
        return personajes
    
    def _recorrer_inorden_recursivo(self, nodo, lista):
        if nodo:
            self._recorrer_inorden_recursivo(nodo.izquierdo, lista)
            lista.append(nodo.personaje)
            self._recorrer_inorden_recursivo(nodo.derecho, lista)