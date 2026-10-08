"""Ejercicio 15 - Entrenadores Pokémon (lista de listas del libro).

Lista principal: entrenadores, ordenados por nombre.
Sublista de cada nodo: los Pokémons del entrenador, ordenados por nombre.
"""

from tda_lista_lista import (Lista, insertar, buscar, barrido, tamanio,
                             lista_vacia)


class Entrenador(object):
    """Registro de un entrenador."""

    def __init__(self, nombre, torneos_ganados, batallas_perdidas,
                 batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

    def __str__(self):
        return (f"{self.nombre} | Torneos ganados: {self.torneos_ganados} | "
                f"Batallas perdidas: {self.batallas_perdidas} | "
                f"Batallas ganadas: {self.batallas_ganadas}")


class Pokemon(object):
    """Registro de un Pokémon."""

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return (f"   {self.nombre} | Nivel: {self.nivel} | "
                f"Tipo: {self.tipo}/{self.subtipo}")


def cargar_entrenador(lista, nombre, torneos, perdidas, ganadas):
    insertar(lista, Entrenador(nombre, torneos, perdidas, ganadas), 'nombre')


def cargar_pokemon(lista, entrenador, nombre, nivel, tipo, subtipo):
    nodo = buscar(lista, entrenador, 'nombre')
    if nodo is not None:
        insertar(nodo.sublista, Pokemon(nombre, nivel, tipo, subtipo), 'nombre')


# a. cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(lista, nombre):
    nodo = buscar(lista, nombre, 'nombre')
    if nodo is not None:
        return tamanio(nodo.sublista)
    return None


# b. entrenadores que hayan ganado más de tres torneos
def mostrar_mas_de_torneos(lista, minimo):
    aux = lista.inicio
    while aux is not None:
        if aux.info.torneos_ganados > minimo:
            print(f"{aux.info.nombre} ({aux.info.torneos_ganados} torneos)")
        aux = aux.sig


# c. Pokémon de mayor nivel del entrenador con más torneos ganados
def pokemon_mayor_nivel_del_campeon(lista):
    if lista_vacia(lista):
        return None
    campeon = lista.inicio
    aux = lista.inicio
    while aux is not None:
        if aux.info.torneos_ganados > campeon.info.torneos_ganados:
            campeon = aux
        aux = aux.sig
    if lista_vacia(campeon.sublista):
        return campeon.info, None
    mayor = campeon.sublista.inicio
    aux = campeon.sublista.inicio
    while aux is not None:
        if aux.info.nivel > mayor.info.nivel:
            mayor = aux
        aux = aux.sig
    return campeon.info, mayor.info


# d. todos los datos de un entrenador y sus Pokémons
def mostrar_entrenador(lista, nombre):
    nodo = buscar(lista, nombre, 'nombre')
    if nodo is not None:
        print(nodo.info)
        print("Pokémons:")
        barrido(nodo.sublista)
    else:
        print(f"{nombre} no está en la lista")


# e. entrenadores cuyo porcentaje de batallas ganadas es mayor a un valor
def mostrar_porcentaje_mayor(lista, porcentaje):
    aux = lista.inicio
    while aux is not None:
        e = aux.info
        total = e.batallas_ganadas + e.batallas_perdidas
        if total > 0:
            p = e.batallas_ganadas * 100 / total
            if p > porcentaje:
                print(f"{e.nombre}: {p:.1f}% de batallas ganadas")
        aux = aux.sig


# f. entrenadores con Pokémons de tipo/subtipo fuego/planta o agua/volador
def mostrar_tipos_combinados(lista):
    aux = lista.inicio
    while aux is not None:
        cumple = False
        p = aux.sublista.inicio
        while p is not None and not cumple:
            tipo = p.info.tipo.lower()
            subtipo = p.info.subtipo.lower()
            if ((tipo == 'fuego' and subtipo == 'planta') or
                    (tipo == 'agua' and subtipo == 'volador')):
                cumple = True
            p = p.sig
        if cumple:
            print(aux.info.nombre)
        aux = aux.sig


# g. promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel(lista, nombre):
    nodo = buscar(lista, nombre, 'nombre')
    if nodo is None or lista_vacia(nodo.sublista):
        return None
    suma = 0
    aux = nodo.sublista.inicio
    while aux is not None:
        suma += aux.info.nivel
        aux = aux.sig
    return suma / tamanio(nodo.sublista)


# h. cuántos entrenadores tienen a un determinado Pokémon
def cuantos_tienen(lista, pokemon):
    cantidad = 0
    aux = lista.inicio
    while aux is not None:
        if buscar(aux.sublista, pokemon, 'nombre') is not None:
            cantidad += 1
        aux = aux.sig
    return cantidad


# i. entrenadores con Pokémons repetidos
# (la sublista está ordenada por nombre, así que los repetidos quedan juntos)
def mostrar_con_repetidos(lista):
    aux = lista.inicio
    while aux is not None:
        p = aux.sublista.inicio
        repetido = None
        while p is not None and p.sig is not None and repetido is None:
            if p.info.nombre == p.sig.info.nombre:
                repetido = p.info.nombre
            p = p.sig
        if repetido is not None:
            print(f"{aux.info.nombre} (repite {repetido})")
        aux = aux.sig


# j. entrenadores que tengan Tyrantrum, Terrakion o Wingull
def mostrar_con_alguno(lista):
    aux = lista.inicio
    while aux is not None:
        sub = aux.sublista
        if (buscar(sub, 'Tyrantrum', 'nombre') is not None or
                buscar(sub, 'Terrakion', 'nombre') is not None or
                buscar(sub, 'Wingull', 'nombre') is not None):
            print(aux.info.nombre)
        aux = aux.sig


if __name__ == '__main__':
    entrenadores = Lista()

    # entrenadores: nombre, torneos ganados, batallas perdidas, batallas ganadas
    cargar_entrenador(entrenadores, 'Ash', 5, 20, 80)
    cargar_entrenador(entrenadores, 'Misty', 2, 30, 70)
    cargar_entrenador(entrenadores, 'Brock', 4, 25, 75)
    cargar_entrenador(entrenadores, 'Gary', 7, 10, 90)
    cargar_entrenador(entrenadores, 'Erika', 1, 40, 60)

    # pokémons: entrenador, nombre, nivel, tipo, subtipo
    cargar_pokemon(entrenadores, 'Ash', 'Pikachu', 60, 'electrico', 'ninguno')
    cargar_pokemon(entrenadores, 'Ash', 'Charizard', 70, 'fuego', 'volador')
    cargar_pokemon(entrenadores, 'Ash', 'Infernape', 65, 'fuego', 'lucha')
    cargar_pokemon(entrenadores, 'Ash', 'Pikachu', 30, 'electrico', 'ninguno')
    cargar_pokemon(entrenadores, 'Misty', 'Starmie', 50, 'agua', 'psiquico')
    cargar_pokemon(entrenadores, 'Misty', 'Gyarados', 55, 'agua', 'volador')
    cargar_pokemon(entrenadores, 'Misty', 'Wingull', 20, 'agua', 'volador')
    cargar_pokemon(entrenadores, 'Brock', 'Onix', 45, 'roca', 'tierra')
    cargar_pokemon(entrenadores, 'Brock', 'Terrakion', 70, 'roca', 'lucha')
    cargar_pokemon(entrenadores, 'Gary', 'Blastoise', 68, 'agua', 'ninguno')
    cargar_pokemon(entrenadores, 'Gary', 'Tyrantrum', 72, 'roca', 'dragon')
    cargar_pokemon(entrenadores, 'Gary', 'Arcanine', 60, 'fuego', 'ninguno')
    cargar_pokemon(entrenadores, 'Erika', 'Vileplume', 40, 'planta', 'veneno')
    cargar_pokemon(entrenadores, 'Erika', 'Torterra', 45, 'planta', 'tierra')
    cargar_pokemon(entrenadores, 'Erika', 'Ponyta', 35, 'fuego', 'planta')

    print("a. Cantidad de Pokémons de Ash:",
          cantidad_pokemons(entrenadores, 'Ash'))

    print("\nb. Entrenadores con más de 3 torneos ganados")
    mostrar_mas_de_torneos(entrenadores, 3)

    print("\nc. Pokémon de mayor nivel del entrenador con más torneos")
    resultado = pokemon_mayor_nivel_del_campeon(entrenadores)
    if resultado is not None:
        print("Entrenador:", resultado[0].nombre)
        print(resultado[1])

    print("\nd. Datos de un entrenador y sus Pokémons")
    mostrar_entrenador(entrenadores, 'Misty')

    print("\ne. Entrenadores con más del 79% de batallas ganadas")
    mostrar_porcentaje_mayor(entrenadores, 79)

    print("\nf. Pokémons fuego/planta o agua/volador")
    mostrar_tipos_combinados(entrenadores)

    print("\ng. Promedio de nivel de los Pokémons de Ash:",
          promedio_nivel(entrenadores, 'Ash'))

    print("\nh. Entrenadores que tienen a Pikachu:",
          cuantos_tienen(entrenadores, 'Pikachu'))

    print("\ni. Entrenadores con Pokémons repetidos")
    mostrar_con_repetidos(entrenadores)

    print("\nj. Entrenadores con Tyrantrum, Terrakion o Wingull")
    mostrar_con_alguno(entrenadores)
