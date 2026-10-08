"""Ejercicio 6 - Superhéroes de comics (usa el TDA lista del libro)."""

from tda_lista_lista import Lista, insertar, eliminar, buscar, barrido


class Superheroe(object):
    """Registro de un superhéroe."""

    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return (f"{self.nombre} | Año: {self.anio_aparicion} | "
                f"Casa: {self.casa} | Biografía: {self.biografia}")


# a. eliminar el nodo que contiene la información de Linterna Verde
def eliminar_superheroe(lista, nombre):
    return eliminar(lista, nombre, 'nombre')


# b. mostrar el año de aparición de Wolverine
def mostrar_anio_aparicion(lista, nombre):
    nodo = buscar(lista, nombre, 'nombre')
    if nodo is not None:
        print(f"{nodo.info.nombre} apareció en {nodo.info.anio_aparicion}")
    else:
        print(f"{nombre} no está en la lista")


# c. cambiar la casa de Dr. Strange a Marvel
def cambiar_casa(lista, nombre, nueva_casa):
    nodo = buscar(lista, nombre, 'nombre')
    if nodo is not None:
        nodo.info.casa = nueva_casa
        print(f"Casa de {nodo.info.nombre} cambiada a {nodo.info.casa}")
    else:
        print(f"{nombre} no está en la lista")


# d. nombres de los superhéroes cuya biografía menciona "traje" o "armadura"
def mostrar_bio_traje_armadura(lista):
    aux = lista.inicio
    while aux is not None:
        bio = aux.info.biografia.lower()
        if 'traje' in bio or 'armadura' in bio:
            print(aux.info.nombre)
        aux = aux.sig


# e. nombre y casa de los superhéroes con aparición anterior a un año
def mostrar_anteriores_a(lista, anio):
    aux = lista.inicio
    while aux is not None:
        if aux.info.anio_aparicion < anio:
            print(f"{aux.info.nombre} - {aux.info.casa}")
        aux = aux.sig


# f. casa a la que pertenece un superhéroe
def mostrar_casa(lista, nombre):
    nodo = buscar(lista, nombre, 'nombre')
    if nodo is not None:
        print(f"{nodo.info.nombre} pertenece a {nodo.info.casa}")
    else:
        print(f"{nombre} no está en la lista")


# g. toda la información de un superhéroe
def mostrar_informacion(lista, nombre):
    nodo = buscar(lista, nombre, 'nombre')
    if nodo is not None:
        print(nodo.info)
    else:
        print(f"{nombre} no está en la lista")


# h. superhéroes cuyo nombre comienza con B, M o S
def mostrar_comienzan_con_bms(lista):
    aux = lista.inicio
    while aux is not None:
        if aux.info.nombre[0].upper() in 'BMS':
            print(aux.info.nombre)
        aux = aux.sig


# i. cuántos superhéroes hay de cada casa
def contar_por_casa(lista):
    marvel = 0
    dc = 0
    aux = lista.inicio
    while aux is not None:
        if aux.info.casa == 'Marvel':
            marvel += 1
        elif aux.info.casa == 'DC':
            dc += 1
        aux = aux.sig
    print(f"Marvel: {marvel} | DC: {dc}")


if __name__ == '__main__':
    superheroes = Lista()
    # la lista queda ordenada por nombre
    insertar(superheroes, Superheroe('Linterna Verde', 1940, 'DC',
             'Piloto que recibe un anillo de poder y viste un traje verde.'), 'nombre')
    insertar(superheroes, Superheroe('Wolverine', 1974, 'Marvel',
             'Mutante con garras de adamantium y factor de curación.'), 'nombre')
    insertar(superheroes, Superheroe('Dr. Strange', 1963, 'DC',
             'Cirujano que se convierte en Hechicero Supremo.'), 'nombre')
    insertar(superheroes, Superheroe('Iron Man', 1963, 'Marvel',
             'Millonario inventor que construye una armadura de alta tecnología.'), 'nombre')
    insertar(superheroes, Superheroe('Capitana Marvel', 1968, 'Marvel',
             'Piloto con poderes cósmicos y un traje rojo y azul.'), 'nombre')
    insertar(superheroes, Superheroe('Mujer Maravilla', 1941, 'DC',
             'Princesa amazona con lazo de la verdad.'), 'nombre')
    insertar(superheroes, Superheroe('Flash', 1940, 'DC',
             'Científico que obtiene supervelocidad.'), 'nombre')
    insertar(superheroes, Superheroe('Star-Lord', 1976, 'Marvel',
             'Mestizo terrestre-alienígena, líder de los Guardianes de la Galaxia.'), 'nombre')
    insertar(superheroes, Superheroe('Batman', 1939, 'DC',
             'Empresario que combate el crimen en Gotham con un traje de murciélago.'), 'nombre')
    insertar(superheroes, Superheroe('Superman', 1938, 'DC',
             'Kryptoniano con superfuerza y vuelo.'), 'nombre')
    insertar(superheroes, Superheroe('Spider-Man', 1962, 'Marvel',
             'Joven picado por una araña radiactiva.'), 'nombre')
    insertar(superheroes, Superheroe('Black Panther', 1966, 'Marvel',
             'Rey de Wakanda con un traje de vibranium.'), 'nombre')

    print("Lista inicial:")
    barrido(superheroes)

    print("\na. Eliminar a Linterna Verde")
    print("Eliminado:", eliminar_superheroe(superheroes, 'Linterna Verde'))

    print("\nb. Año de aparición de Wolverine")
    mostrar_anio_aparicion(superheroes, 'Wolverine')

    print("\nc. Cambiar la casa de Dr. Strange")
    cambiar_casa(superheroes, 'Dr. Strange', 'Marvel')

    print("\nd. Biografía con 'traje' o 'armadura'")
    mostrar_bio_traje_armadura(superheroes)

    print("\ne. Aparición anterior a 1963")
    mostrar_anteriores_a(superheroes, 1963)

    print("\nf. Casa de Capitana Marvel y Mujer Maravilla")
    mostrar_casa(superheroes, 'Capitana Marvel')
    mostrar_casa(superheroes, 'Mujer Maravilla')

    print("\ng. Información de Flash y Star-Lord")
    mostrar_informacion(superheroes, 'Flash')
    mostrar_informacion(superheroes, 'Star-Lord')

    print("\nh. Nombres que comienzan con B, M o S")
    mostrar_comienzan_con_bms(superheroes)

    print("\ni. Cantidad por casa")
    contar_por_casa(superheroes)
