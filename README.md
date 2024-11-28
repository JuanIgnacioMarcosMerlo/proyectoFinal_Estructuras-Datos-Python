# Documentación del Proyecto: Juego Basado en Dragon Ball

## Índice
- [Documentación del Proyecto: Juego Basado en Dragon Ball](#documentación-del-proyecto-juego-basado-en-dragon-ball)
  - [Índice](#índice)
  - [Descripción del Proyecto](#descripción-del-proyecto)
    - [Características Principales:](#características-principales)
  - [Estructuras de Datos Utilizadas y Justificación](#estructuras-de-datos-utilizadas-y-justificación)
    - [1. **Árbol Binario: `ArbolPersonajes`**](#1-árbol-binario-arbolpersonajes)
      - [Justificación:](#justificación)
      - [Funcionalidad:](#funcionalidad)
    - [2. **Árbol General: `ArbolHabilidades`**](#2-árbol-general-arbolhabilidades)
      - [Justificación:](#justificación-1)
      - [Funcionalidad:](#funcionalidad-1)
    - [3. **Cola de Prioridad: `ColaDePrioridad`**](#3-cola-de-prioridad-coladeprioridad)
      - [Justificación:](#justificación-2)
      - [Funcionalidad:](#funcionalidad-2)
    - [4. **Lista Enlazada: `ListaEnlazadaTransformaciones`**](#4-lista-enlazada-listaenlazadatransformaciones)
      - [Justificación:](#justificación-3)
      - [Funcionalidad:](#funcionalidad-3)
    - [5. **Grafo: `Grafo`**](#5-grafo-grafo)
      - [Justificación:](#justificación-4)
      - [Funcionalidad:](#funcionalidad-4)
  - [Explicación del Código](#explicación-del-código)
    - [Creación de Personajes](#creación-de-personajes)
    - [Gestión de Transformaciones](#gestión-de-transformaciones)
    - [Combates](#combates)
    - [Torneos](#torneos)
    - [Exploración del Mapa](#exploración-del-mapa)
  - [Algoritmos de Búsqueda y Ordenamiento](#algoritmos-de-búsqueda-y-ordenamiento)
    - [DFS (Depth-First Search)](#dfs-depth-first-search)
      - [Justificación:](#justificación-5)
      - [Funcionalidad:](#funcionalidad-5)
    - [BFS (Breadth-First Search)](#bfs-breadth-first-search)
      - [Justificación:](#justificación-6)
      - [Funcionalidad:](#funcionalidad-6)
    - [Ordenamiento Topológico](#ordenamiento-topológico)
      - [Justificación:](#justificación-7)
      - [Funcionalidad:](#funcionalidad-7)
    - [Dijkstra](#dijkstra)
      - [Justificación:](#justificación-8)
      - [Funcionalidad:](#funcionalidad-8)
  - [Conclusión](#conclusión)
  - [Integrantes](#integrantes)

---

## Descripción del Proyecto

Este proyecto es un juego basado en el universo de **Dragon Ball**, donde los jugadores pueden crear personajes, gestionar sus habilidades y transformaciones, y enfrentarlos en combates. Además, se puede organizar un torneo de personajes y explorar un mapa que representa el universo de Dragon Ball. El juego utiliza varias estructuras de datos para gestionar de manera eficiente los personajes, habilidades, transformaciones y el mapa del juego.

### Características Principales:
- **Creación de personajes**: Los personajes tienen atributos como nivel de poder, habilidades y transformaciones.
- **Sistema de habilidades**: Cada personaje tiene habilidades que pueden ser mejoradas o transformadas.
- **Sistema de combates**: Los personajes pueden pelear entre sí, y su rendimiento se basa en su nivel de poder y las transformaciones activadas.
- **Torneos**: Los personajes compiten en torneos, donde el personaje con el mayor nivel de poder avanza.
- **Exploración de un mapa**: Usando grafos, el jugador puede explorar planetas, enfrentar enemigos y recolectar esferas del dragón.

---

## Estructuras de Datos Utilizadas y Justificación

### 1. **Árbol Binario: `ArbolPersonajes`**

#### Justificación:
El **árbol binario** se utiliza para organizar a los personajes en el juego. Los personajes se insertan en el árbol en función de su nivel de poder, lo que permite buscar y ordenar los personajes de manera eficiente.

- **Búsqueda eficiente**: Las operaciones de búsqueda, inserción y eliminación en un árbol binario se realizan en **O(log n)**, lo que permite manejar grandes cantidades de personajes de manera eficiente.
- **Ordenación automática**: El árbol mantiene automáticamente a los personajes ordenados por su nivel de poder, lo que facilita la realización de combates y la creación de torneos.

#### Funcionalidad:
- La clase `ArbolPersonajes` permite insertar personajes en el árbol y realizar un recorrido inorden para obtener una lista de personajes ordenada por nivel de poder.
- También proporciona un método para buscar al personaje con el mayor nivel de poder, lo cual es útil para determinar quién es el más fuerte en el juego.

### 2. **Árbol General: `ArbolHabilidades`**

#### Justificación:
Las habilidades de los personajes tienen una estructura jerárquica. Una habilidad puede tener mejoras o transformaciones que dependen de la habilidad anterior. Un **árbol general** es ideal para modelar esta relación de dependencias.

- **Relación jerárquica de habilidades**: Cada habilidad puede tener varias sub-habilidades, y un árbol general permite representar estas relaciones de forma clara.
- **Gestión dinámica de habilidades**: Se pueden agregar nuevas habilidades o transformaciones de manera dinámica durante el juego.

#### Funcionalidad:
- La clase `ArbolHabilidades` permite agregar habilidades a personajes, estructurándolas en una jerarquía.
- También permite listar todas las habilidades disponibles de un personaje, facilitando la visualización y gestión de las habilidades durante el juego.

### 3. **Cola de Prioridad: `ColaDePrioridad`**

#### Justificación:
En el juego, los combates entre personajes deben priorizar al personaje con el mayor nivel de poder. La **cola de prioridad** es perfecta para este tipo de situaciones, ya que siempre garantiza que el personaje más fuerte esté disponible para el próximo combate.

- **Prioridad en combates**: La cola de prioridad asegura que el personaje más fuerte (con el mayor nivel de poder) sea el primero en combatir.
- **Eficiencia en operaciones**: Las operaciones de inserción y extracción se realizan en **O(log n)**, manteniendo siempre el orden de los personajes según su nivel de poder.

#### Funcionalidad:
- La clase `ColaDePrioridad` gestiona una cola de personajes en la que siempre se extrae el personaje con el mayor nivel de poder.
- Utiliza un enfoque basado en un **heap binario** para realizar las inserciones y extracciones de manera eficiente.

### 4. **Lista Enlazada: `ListaEnlazadaTransformaciones`**

#### Justificación:
Las transformaciones en el juego se gestionan dinámicamente. Un **listado dinámico** como la **lista enlazada** es ideal para almacenar transformaciones que un personaje puede aprender a medida que avanza en el juego.

- **Dinámica y flexible**: La lista enlazada permite agregar nuevas transformaciones sin tener que reorganizar toda la estructura, lo que facilita la expansión del juego.
- **Acceso secuencial**: Las transformaciones pueden recorrerse de forma secuencial, lo cual es útil cuando se desean mostrar todas las transformaciones disponibles para un personaje.

#### Funcionalidad:
- La clase `ListaEnlazadaTransformaciones` almacena las transformaciones disponibles para un personaje en una lista enlazada.
- Permite agregar nuevas transformaciones, buscar una transformación específica y listar todas las transformaciones disponibles.

### 5. **Grafo: `Grafo`**

#### Justificación:
El **grafo** se utiliza para representar el mapa del juego, donde cada planeta es un nodo y las conexiones entre planetas son las aristas. Este modelo es perfecto para representar las relaciones entre los diferentes puntos del universo de Dragon Ball.

- **Representación del mapa**: Los grafos permiten modelar de manera eficiente las conexiones entre planetas y la información asociada a ellos, como enemigos y esferas del dragón.
- **Recorridos eficientes**: Los algoritmos de búsqueda como **DFS** (Depth-First Search) y **BFS** (Breadth-First Search) permiten explorar el mapa del universo y encontrar los caminos óptimos entre planetas.

#### Funcionalidad:
- La clase `Grafo` permite agregar planetas y sus respectivas conexiones.
- Proporciona métodos para recorrer el grafo y encontrar caminos entre planetas, lo cual es fundamental para la exploración y la recolección de esferas del dragón.

---

## Explicación del Código

### Creación de Personajes

La función `crear_personaje` permite al jugador crear un nuevo personaje interactuando con el sistema. Se le asignan valores como nivel de poder, habilidades, raza, salud y poder de ataque. Una vez creado, el personaje se inserta en el árbol de personajes y en la cola de prioridad para los combates.

### Gestión de Transformaciones

La función `agregar_transformaciones_personaje` permite agregar nuevas transformaciones a los personajes durante el juego. Se utilizan listas enlazadas para almacenar las transformaciones, lo que permite agregar nuevas transformaciones dinámicamente. También se ofrece la opción de transformar a los personajes durante el combate, con la posibilidad de añadir nuevas transformaciones si es necesario.

### Combates

La función `combate` permite a dos personajes enfrentarse. Ambos personajes tienen la opción de transformarse antes del combate. Si no tienen transformaciones disponibles, se les pregunta si desean agregar una. El combate se resuelve en función del nivel de poder de los personajes, y el ganador sube de nivel.

### Torneos

La función `torneo` organiza combates entre los personajes que se encuentran en la cola de prioridad. El ganador de cada combate sigue compitiendo en la siguiente ronda hasta que se determine el campeón.

### Exploración del Mapa

Se utiliza un grafo para modelar el mapa del universo de Dragon Ball. Los planetas son nodos del grafo, y las conexiones entre ellos son las aristas. El jugador puede recorrer el mapa utilizando algoritmos de búsqueda como **DFS** y **BFS**.

---

## Algoritmos de Búsqueda y Ordenamiento

### DFS (Depth-First Search)

#### Justificación:
El algoritmo **DFS** se utiliza para recorrer el grafo de habilidades en un orden en el que se procesen todas las habilidades y sus dependencias. Esto es útil para determinar el orden correcto en el que un personaje debe aprender sus habilidades, siguiendo las relaciones jerárquicas entre ellas.

#### Funcionalidad:
- El DFS permite recorrer el grafo de habilidades y realizar un **ordenamiento topológico**. Esto asegura que las habilidades se aprendan en el orden correcto, siguiendo sus dependencias.

---

### BFS (Breadth-First Search)

#### Justificación:
El **BFS** es utilizado para recorrer el mapa del juego representado como un grafo, garantizando que el jugador visite todos los planetas para recolectar esferas del dragón de forma eficiente.

#### Funcionalidad:
- El BFS recorre el grafo de manera exhaustiva, asegurando que se visite cada planeta, lo cual es útil cuando el jugador necesita recolectar todas las esferas del dragón.

---

### Ordenamiento Topológico

#### Justificación:
El **ordenamiento topológico** es utilizado para ordenar las habilidades del personaje en el orden en que deben ser aprendidas, basándose en las dependencias entre habilidades.

#### Funcionalidad:
- Este algoritmo asegura que las habilidades de un personaje se aprendan en el orden correcto, comenzando por las habilidades base y avanzando hasta las transformaciones más poderosas.

---

### Dijkstra

#### Justificación:
El algoritmo de **Dijkstra** se sugiere para encontrar el camino más eficiente entre planetas en el universo del juego, optimizando el uso de los recursos (por ejemplo, el combustible para viajar entre planetas).

#### Funcionalidad:
- El algoritmo de Dijkstra calcula el camino más corto entre dos planetas, minimizando el costo del viaje, que se puede interpretar como la cantidad de combustible necesario para viajar entre planetas en el grafo.

---

## Conclusión

Este proyecto demuestra cómo las **estructuras de datos avanzadas** como **árboles binarios**, **colas de prioridad**, **listas enlazadas** y **grafos** pueden usarse para crear un juego eficiente y dinámico. Cada una de estas estructuras se seleccionó en función de su capacidad para gestionar diferentes aspectos del juego, como la organización de los personajes, la gestión de habilidades y transformaciones, la priorización de combates, y la navegación en el mapa.

La combinación de estas estructuras de datos no solo mejora el rendimiento y la escalabilidad del juego, sino que también permite una jugabilidad fluida y flexible, ofreciendo una experiencia rica y optimizada para el jugador. Además, la implementación de algoritmos de búsqueda como **DFS**, **BFS**, y **Dijkstra** ayuda a garantizar que la exploración y el avance del juego se realicen de manera eficiente, mejorando la experiencia del usuario.

---

## Integrantes

- Juan Ignacio Marcos Merlo

- Santiago Logarzo
