# -*- coding: utf-8 -*-
"""
Ejercicio 10 - Gestión de Notificaciones
"""

from collections import deque

def hora_a_minutos(hora_str):
    # Convierte "HH:MM" a minutos para facilitar comparaciones numéricas
    partes = hora_str.split(":")
    return int(partes[0]) * 60 + int(partes[1])

def eliminar_notificaciones_facebook(cola):
    print("\n--- Eliminando notificaciones de Facebook ---")
    tamanio = len(cola)
    for _ in range(tamanio):
        notificacion = cola.popleft()
        if notificacion["aplicacion"].lower() != "facebook":
            cola.append(notificacion)
        else:
            print(f"  [Eliminada] Facebook - {notificacion['hora']}: {notificacion['mensaje']}")

def mostrar_twitter_python(cola):
    print("\n--- Buscando notificaciones de Twitter sobre 'Python' (sin perder datos) ---")
    tamanio = len(cola)
    for _ in range(tamanio):
        notificacion = cola.popleft()
        es_twitter = notificacion["aplicacion"].lower() == "twitter"
        contiene_python = "python" in notificacion["mensaje"].lower()
        
        if es_twitter and contiene_python:
            print(f"  - {notificacion['hora']} | {notificacion['aplicacion']}: {notificacion['mensaje']}")
        
        # Se vuelve a encolar al final para no perder datos
        cola.append(notificacion)

def filtrar_rango_pila(cola):
    print("\n--- Filtrando rango [11:43 - 15:57] usando una Pila ---")
    pila_temporal = []
    limite_inf = hora_a_minutos("11:43")
    limite_sup = hora_a_minutos("15:57")
    tamanio = len(cola)
    
    for _ in range(tamanio):
        notificacion = cola.popleft()
        minutos = hora_a_minutos(notificacion["hora"])
        
        if limite_inf <= minutos <= limite_sup:
            pila_temporal.append(notificacion) # Apilar (LIFO)
            
        cola.append(notificacion)
        
    print(f"Cantidad de notificaciones en el rango: {len(pila_temporal)}")
    print("Contenido de la pila (LIFO, del más reciente al más antiguo):")
    
    # Mostrar desapilando los elementos
    while pila_temporal:
        notif = pila_temporal.pop()
        print(f"  - {notif['hora']} | {notif['aplicacion']}: {notif['mensaje']}")
        
    return len(pila_temporal)

def mostrar_cola(cola, titulo="Estado de la Cola"):
    print(f"\n=== {titulo} ===")
    for item in cola:
        print(f"  [{item['hora']}] {item['aplicacion']}: {item['mensaje']}")
    print("=========================================")

if __name__ == "__main__":
    cola_notificaciones = deque()
    
    datos_iniciales = [
        {"hora": "08:30", "aplicacion": "WhatsApp", "mensaje": "Hola! ¿Cómo estás?"},
        {"hora": "10:15", "aplicacion": "Facebook", "mensaje": "A Juan Pérez le gustó tu foto."},
        {"hora": "11:45", "aplicacion": "Twitter", "mensaje": "Aprendiendo Python básico en mi carrera de sistemas!"},
        {"hora": "12:30", "aplicacion": "Facebook", "mensaje": "Recordatorio de cumpleaños de María."},
        {"hora": "14:10", "aplicacion": "Twitter", "mensaje": "La ciencia de datos con Python es fascinante #python"},
        {"hora": "15:50", "aplicacion": "Instagram", "mensaje": "Nuevo seguidor."},
        {"hora": "15:58", "aplicacion": "Twitter", "mensaje": "Noticia de último minuto en Python."},
        {"hora": "16:20", "aplicacion": "Facebook", "mensaje": "Te han etiquetado en una publicación."},
        {"hora": "18:00", "aplicacion": "Twitter", "mensaje": "Buenas noches a toda la comunidad!"}
    ]
    
    for dato in datos_iniciales:
        cola_notificaciones.append(dato)
        
    mostrar_cola(cola_notificaciones, "Cola Inicial")
    mostrar_twitter_python(cola_notificaciones)
    filtrar_rango_pila(cola_notificaciones)
    eliminar_notificaciones_facebook(cola_notificaciones)
    mostrar_cola(cola_notificaciones, "Cola Final")
