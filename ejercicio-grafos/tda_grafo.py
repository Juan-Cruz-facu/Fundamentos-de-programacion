from math import inf

# ==========================================
# ESTRUCTURAS AUXILIARES DEL LIBRO (Pila, Cola, Heap)
# ==========================================

class nodoPila(object):
    info, sig = None, None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0

def apilar(pila, dato):
    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

def desapilar(pila):
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return x

def pila_vacia(pila):
    return pila.cima is None


class nodoCola(object):
    info, sig = None, None

class Cola(object):
    def __init__(self):
        self.frente, self.final = None, None
        self.tamanio = 0

def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return dato

def cola_vacia(cola):
    return cola.frente is None


class Heap(object):
    """Montículo de mínimo para Dijkstra y Prim."""
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio

def intercambio(vector, indice1, indice2):
    vector[indice1], vector[indice2] = vector[indice2], vector[indice1]

def flotar(heap, indice):
    while indice > 0 and heap.vector[indice][0] < heap.vector[(indice - 1) // 2][0]:
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre

def hundir(heap, indice):
    hijo_izq = (indice * 2) + 1
    control = True
    while control and hijo_izq < heap.tamanio:
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if hijo_der < heap.tamanio:
            if heap.vector[hijo_der][0] < heap.vector[hijo_izq][0]:
                aux = hijo_der
        if heap.vector[indice][0] > heap.vector[aux][0]:
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
        else:
            control = False

def agregar_h(heap, dato):
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1

def quitar_h(heap):
    intercambio(heap.vector, 0, heap.tamanio - 1)
    dato = heap.vector[heap.tamanio - 1]
    heap.tamanio -= 1
    hundir(heap, 0)
    return dato

def arribo_h(heap, dato, prioridad):
    agregar_h(heap, [prioridad, dato])

def atencion_h(heap):
    return quitar_h(heap)

def heap_vacio(heap):
    return heap.tamanio == 0

def buscar_h(heap, buscado):
    for i in range(heap.tamanio):
        if heap.vector[i][1][0].info == buscado:
            return i
    return -1

def cambiar_prioridad(heap, indice, prioridad):
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if prioridad < prioridad_anterior:
        flotar(heap, indice)
    elif prioridad > prioridad_anterior:
        hundir(heap, indice)


# ==========================================
# TDA GRAFO (Implementación Lista de Listas de Adyacencia del Libro)
# ==========================================

class nodoArista(object):
    """Clase nodo arista."""
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None

class nodoVertice(object):
    """Clase nodo vértice."""
    def __init__(self, info, datos_extra=None):
        self.info = info
        self.datos_extra = datos_extra
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo(object):
    """Clase grafo implementación lista de listas de adyacencia."""
    def __init__(self, dirigido=True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0

class Arista(object):
    """Clase lista de aristas implementación sobre lista."""
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato, datos_extra=None):
    """Inserta un vértice al grafo."""
    nodo = nodoVertice(dato, datos_extra)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info < nodo.info:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

def agregar_arista(origen, dato, destino):
    """Agrega la arista desde el vértice origen al destino."""
    nodo = nodoArista(dato, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

def insertar_arista(grafo, dato, origen, destino):
    """Inserta una arista desde el vértice origen al destino."""
    agregar_arista(origen.adyacentes, dato, destino.info)
    if not grafo.dirigido:
        agregar_arista(destino.adyacentes, dato, origen.info)

def buscar_vertice(grafo, buscado):
    """Devuelve la dirección del elemento buscado."""
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux

def buscar_arista(vertice, buscado):
    """Devuelve la dirección del elemento buscado."""
    aux = vertice.adyacentes.inicio
    while aux is not None and aux.destino != buscado:
        aux = aux.sig
    return aux

def tamanio(grafo):
    """Devuelve el número de vértices en el grafo."""
    return grafo.tamanio

def grafo_vacio(grafo):
    """Devuelve true si el grafo está vacío."""
    return grafo.inicio is None

def eliminar_arista(vertice_adyacentes, destino):
    """Elimina una arista del vértice y la devuelve si la encuentra."""
    x = None
    if vertice_adyacentes.inicio is not None:
        if vertice_adyacentes.inicio.destino == destino:
            x = vertice_adyacentes.inicio.info
            vertice_adyacentes.inicio = vertice_adyacentes.inicio.sig
            vertice_adyacentes.tamanio -= 1
        else:
            ant = vertice_adyacentes.inicio
            act = vertice_adyacentes.inicio.sig
            while act is not None and act.destino != destino:
                ant = act
                act = act.sig
            if act is not None:
                x = act.info
                ant.sig = act.sig
                vertice_adyacentes.tamanio -= 1
    return x

def eliminar_arista_grafo(grafo, origen, destino):
    """Elimina una arista entre origen y destino (contempla grafo no dirigido)."""
    x = eliminar_arista(origen.adyacentes, destino.info)
    if not grafo.dirigido:
        eliminar_arista(destino.adyacentes, origen.info)
    return x

def marcar_no_visitado(grafo):
    """Marca todos los vértices del grafo como no visitados."""
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig

def barrido_profundidad(grafo, vertice):
    """Barrido en profundidad del grafo."""
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(f"  -> {vertice.info}")
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if not adyacente.visitado:
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig

def barrido_amplitud(grafo, vertice):
    """Barrido en amplitud del grafo."""
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(f"  -> {nodo.info}")
                adyacentes = nodo.adyacentes.inicio
                while adyacentes is not None:
                    adyacente = buscar_vertice(grafo, adyacentes.destino)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig

def dijkstra(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino más corto."""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info == origen:
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig

    while not heap_vacio(no_visitados):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscar_h(no_visitados, aux.destino)
            if pos != -1:
                if no_visitados.vector[pos][0] > dato[0] + aux.info:
                    no_visitados.vector[pos][1][1] = dato[1][0].info
                    cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino

def recuperar_camino(pila_camino, destino):
    """Reconstruye el camino y el peso total a partir de la pila devuelta por Dijkstra."""
    camino = []
    peso_total = None
    fin = destino
    while not pila_vacia(pila_camino):
        dato = desapilar(pila_camino)
        if dato[1][0].info == fin:
            if peso_total is None:
                peso_total = dato[0]
            camino.insert(0, dato[1][0].info)
            fin = dato[1][1]
    return camino, peso_total

def kruskal(grafo):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(tamanio(grafo) ** 2)
    aux = grafo.inicio
    while aux is not None:
        bosque.append([aux.info])
        adyacentes = aux.adyacentes.inicio
        while adyacentes is not None:
            arribo_h(aristas, [aux.info, adyacentes.destino], adyacentes.info)
            adyacentes = adyacentes.sig
        aux = aux.sig

    arbol_expansion = []
    peso_total = 0
    while len(bosque) > 1 and not heap_vacio(aristas):
        dato = atencion_h(aristas)
        peso = dato[0]
        origen = dato[1][0]
        destino = dato[1][1]

        conjunto_origen = None
        conjunto_destino = None

        for subconjunto in bosque:
            if origen in subconjunto:
                conjunto_origen = subconjunto
            if destino in subconjunto:
                conjunto_destino = subconjunto

        if conjunto_origen is not conjunto_destino:
            bosque.remove(conjunto_origen)
            bosque.remove(conjunto_destino)
            bosque.append(conjunto_origen + conjunto_destino)
            arbol_expansion.append((origen, destino, peso))
            peso_total += peso

    return arbol_expansion, peso_total
