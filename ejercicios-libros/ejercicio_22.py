# -*- coding: utf-8 -*-
"""
Ejercicio 22 - MCU Personajes
"""

from collections import deque

def personaje_de_superheroe(cola, nombre_superheroe):
    # Determinar el nombre del personaje detrás del superhéroe
    tamanio = len(cola)
    personaje_encontrado = None
    for _ in range(tamanio):
        p = cola.popleft()
        if p["nombre_superheroe"].strip().lower() == nombre_superheroe.strip().lower():
            personaje_encontrado = p["nombre_personaje"]
        cola.append(p)
    
    if personaje_encontrado:
        print(f"Personaje de '{nombre_superheroe}': {personaje_encontrado}")
    return personaje_encontrado

def mostrar_superheroes_femeninos(cola):
    # Mostrar nombres de superhéroes femeninos
    print("\n--- Superhéroes Femeninos ---")
    tamanio = len(cola)
    for _ in range(tamanio):
        p = cola.popleft()
        if p["genero"].upper() == "F":
            print(f"  - {p['nombre_superheroe']}")
        cola.append(p)

def mostrar_personajes_masculinos(cola):
    # Mostrar nombres de personajes masculinos
    print("\n--- Personajes Masculinos ---")
    tamanio = len(cola)
    for _ in range(tamanio):
        p = cola.popleft()
        if p["genero"].upper() == "M":
            print(f"  - {p['nombre_personaje']}")
        cola.append(p)

def superheroe_de_personaje(cola, nombre_personaje):
    # Determinar el superhéroe asociado al nombre de personaje real
    tamanio = len(cola)
    superheroe_encontrado = None
    for _ in range(tamanio):
        p = cola.popleft()
        if p["nombre_personaje"].strip().lower() == nombre_personaje.strip().lower():
            superheroe_encontrado = p["nombre_superheroe"]
        cola.append(p)
        
    if superheroe_encontrado:
        print(f"Superhéroe de '{nombre_personaje}': {superheroe_encontrado}")
    return superheroe_encontrado

def mostrar_datos_letra_s(cola):
    # Mostrar datos cuyos nombres comiencen con "S"
    print("\n--- Personajes o Superhéroes que comienzan con 'S' ---")
    tamanio = len(cola)
    for _ in range(tamanio):
        p = cola.popleft()
        if p["nombre_personaje"].strip().upper().startswith("S") or p["nombre_superheroe"].strip().upper().startswith("S"):
            print(f"  Personaje: {p['nombre_personaje']} | Superhéroe: {p['nombre_superheroe']} | Género: {p['genero']}")
        cola.append(p)

def buscar_carol_danvers(cola):
    # Comprobar si Carol Danvers está en la cola e indicar su superhéroe
    tamanio = len(cola)
    encontrada = False
    superheroe_nombre = None
    for _ in range(tamanio):
        p = cola.popleft()
        if p["nombre_personaje"].strip().lower() == "carol danvers":
            encontrada = True
            superheroe_nombre = p["nombre_superheroe"]
        cola.append(p)
        
    if encontrada:
        print(f"Carol Danvers está en la cola. Su superhéroe es '{superheroe_nombre}'")
    else:
        print("Carol Danvers no se encuentra en la cola.")
    return encontrada, superheroe_nombre

def mostrar_cola_mcu(cola, titulo="Estado de la Cola MCU"):
    print(f"\n==================== {titulo} ====================")
    for p in cola:
        print(f"  [{p['genero']}] {p['nombre_personaje']} es '{p['nombre_superheroe']}'")
    print("=========================================================")

if __name__ == "__main__":
    cola_mcu = deque()
    
    personajes = [
        {"nombre_personaje": "Tony Stark", "nombre_superheroe": "Iron Man", "genero": "M"},
        {"nombre_personaje": "Steve Rogers", "nombre_superheroe": "Capitán América", "genero": "M"},
        {"nombre_personaje": "Natasha Romanoff", "nombre_superheroe": "Black Widow", "genero": "F"},
        {"nombre_personaje": "Carol Danvers", "nombre_superheroe": "Capitana Marvel", "genero": "F"},
        {"nombre_personaje": "Scott Lang", "nombre_superheroe": "Ant-Man", "genero": "M"},
        {"nombre_personaje": "Wanda Maximoff", "nombre_superheroe": "Scarlet Witch", "genero": "F"},
        {"nombre_personaje": "Stephen Strange", "nombre_superheroe": "Doctor Strange", "genero": "M"},
        {"nombre_personaje": "Sam Wilson", "nombre_superheroe": "Falcon", "genero": "M"},
        {"nombre_personaje": "Shuri", "nombre_superheroe": "Shuri", "genero": "F"}
    ]
    
    for p in personajes:
        cola_mcu.append(p)
        
    mostrar_cola_mcu(cola_mcu, "Cola Inicial")
    
    personaje_de_superheroe(cola_mcu, "Capitana Marvel")
    mostrar_superheroes_femeninos(cola_mcu)
    mostrar_personajes_masculinos(cola_mcu)
    superheroe_de_personaje(cola_mcu, "Scott Lang")
    mostrar_datos_letra_s(cola_mcu)
    buscar_carol_danvers(cola_mcu)
    
    mostrar_cola_mcu(cola_mcu, "Cola Final")

