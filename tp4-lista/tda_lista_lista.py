"""TDA lista simplemente enlazada y lista de listas (Capítulo VIII del libro).

Incluye la función criterio y las funciones insertar, eliminar, buscar,
barrido, tamanio y lista_vacia con el parámetro opcional `campo`.
Cada nodo tiene además el atributo `sublista` (una Lista) para poder
usar la estructura como lista de listas.
"""


class nodoLista(object):
    """Clase nodo lista."""

    info, sig, sublista = None, None, None


class Lista(object):
    """Clase lista simplemente enlazada."""

    def __init__(self):
        """Crea una lista vacia."""
        self.inicio = None
        self.tamanio = 0


def criterio(dato, campo=None):
    """Determina el campo por el cual se debe comparar el dato."""
    dic = {}
    if hasattr(dato, '__dict__'):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]


def insertar(lista, dato, campo=None):
    """Inserta el dato pasado en la lista."""
    nodo = nodoLista()
    nodo.info = dato
    nodo.sublista = Lista()
    if (lista.inicio is None) or (criterio(lista.inicio.info, campo) >
                                  criterio(dato, campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while (act is not None and criterio(act.info, campo) <
               criterio(dato, campo)):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1


def lista_vacia(lista):
    """Devuelve true si la lista esta vacia."""
    return lista.inicio is None


def eliminar(lista, clave, campo=None):
    """Elimina un elemento de la lista y lo devuelve si lo encuentra."""
    dato = None
    if (criterio(lista.inicio.info, campo) == criterio(clave, campo)):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while (actual is not None and criterio(actual.info, campo) !=
               criterio(clave, campo)):
            anterior = anterior.sig
            actual = actual.sig
        if (actual is not None):
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamanio -= 1
    return dato


def tamanio(lista):
    """Devuelve el numero de elementos en la lista."""
    return lista.tamanio


def buscar(lista, buscado, campo=None):
    """Devuelve la direccion del elemento buscado."""
    aux = lista.inicio
    while (aux is not None and criterio(aux.info, campo) !=
           criterio(buscado, campo)):
        aux = aux.sig
    return aux


def barrido(lista):
    """Realiza un barrido de la lista mostrando sus valores."""
    aux = lista.inicio
    while (aux is not None):
        print(aux.info)
        aux = aux.sig
