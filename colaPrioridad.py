class ColaDePrioridad:
    def __init__(self):
        self.cola = []

    def agregar_a_cola(self, personaje):
        self.cola.append(personaje)
        self._subir(len(self.cola) - 1)

    def extraer_de_cola(self):
        if len(self.cola) == 0:
            return None
        if len(self.cola) == 1:
            return self.cola.pop()

        self._intercambiar(0, len(self.cola) - 1)
        personaje_max = self.cola.pop()
        self._bajar(0)
        return personaje_max

    def esta_vacia(self):
        return len(self.cola) == 0

    def listar_personajes(self):
        print("\n=== Personajes en la cola de prioridad ===")
        for personaje in sorted(self.cola, key=lambda x: -x.nivel_poder):
            print(f"{personaje.nombre} (Nivel de Poder: {personaje.nivel_poder})")

    def _subir(self, index):
        padre = (index - 1) // 2  # Índice del padre
        while index > 0 and self.cola[index].nivel_poder > self.cola[padre].nivel_poder:
            self._intercambiar(index, padre)
            index = padre
            padre = (index - 1) // 2

    def _bajar(self, index):
        hijo_izquierdo = 2 * index + 1
        hijo_derecho = 2 * index + 2
        mayor = index

        if hijo_izquierdo < len(self.cola) and self.cola[hijo_izquierdo].nivel_poder > self.cola[mayor].nivel_poder:
            mayor = hijo_izquierdo

        if hijo_derecho < len(self.cola) and self.cola[hijo_derecho].nivel_poder > self.cola[mayor].nivel_poder:
            mayor = hijo_derecho

        if mayor != index:
            self._intercambiar(index, mayor)
            self._bajar(mayor)

    def _intercambiar(self, i, j):
        self.cola[i], self.cola[j] = self.cola[j], self.cola[i]