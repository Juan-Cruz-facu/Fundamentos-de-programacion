from tda_grafo import (
    Grafo,
    insertar_vertice,
    insertar_arista,
    buscar_vertice,
    dijkstra,
    recuperar_camino,
    kruskal,
)

# Grafo no dirigido para representar los ambientes de la casa
casa = Grafo(dirigido=False)

# ==============================================================================
# a. Cada vértice representa un ambiente de una casa: cocina, comedor, cochera,
#    quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar,
#    terraza, patio
# ==============================================================================
ambientes = [
    "cocina",
    "comedor",
    "cochera",
    "quincho",
    "baño 1",
    "baño 2",
    "habitación 1",
    "habitación 2",
    "sala de estar",
    "terraza",
    "patio",
]

for ambiente in ambientes:
    insertar_vertice(casa, ambiente)


# ==============================================================================
# b. Cargar al menos tres aristas a cada vértice, y a dos de estas cárguele
#    cinco, el peso de la arista es la distancia entre los ambientes, se debe
#    cargar en metros
# ==============================================================================
# Diseño de conexiones:
# - "comedor" tiene 5 aristas (cocina, sala de estar, patio, baño 1, terraza)
# - "sala de estar" tiene 5 aristas (comedor, habitación 1, habitación 2, baño 1, terraza)
# - El resto de los ambientes tiene entre 3 y 4 aristas (todos >= 3 aristas)
distancias_metros = [
    # Aristas de comedor (5 conexiones)
    ("comedor", "cocina", 4),
    ("comedor", "sala de estar", 5),
    ("comedor", "patio", 7),
    ("comedor", "baño 1", 6),
    ("comedor", "terraza", 9),
    # Aristas adicionales de sala de estar (completa 5 conexiones)
    ("sala de estar", "habitación 1", 6),
    ("sala de estar", "habitación 2", 5),
    ("sala de estar", "baño 1", 3),
    ("sala de estar", "terraza", 8),
    # Resto de conexiones para que cada ambiente tenga al menos 3 aristas
    ("cocina", "cochera", 6),
    ("cocina", "patio", 5),
    ("cochera", "patio", 8),
    ("cochera", "quincho", 12),
    ("quincho", "patio", 6),
    ("quincho", "baño 2", 4),
    ("quincho", "terraza", 10),
    ("habitación 1", "baño 1", 2),
    ("habitación 1", "habitación 2", 4),
    ("habitación 2", "baño 2", 3),
    ("baño 2", "terraza", 7),
]

for amb_origen, amb_destino, metros in distancias_metros:
    v_orig = buscar_vertice(casa, amb_origen)
    v_dest = buscar_vertice(casa, amb_destino)
    insertar_arista(casa, metros, v_orig, v_dest)

print("=" * 70)
print("PUNTO A y B: Verificación de ambientes y cantidad de aristas cargadas")
print("=" * 70)
aux = casa.inicio
while aux is not None:
    print(f"  Ambiente: {aux.info:<15} | Cantidad de conexiones (aristas): {aux.adyacentes.tamanio}")
    aux = aux.sig


# ==============================================================================
# c. Obtener el árbol de expansión mínima y determine cuántos metros de cables
#    se necesitan para conectar todos los ambientes
# ==============================================================================
print("\n" + "=" * 70)
print("PUNTO C: Árbol de expansión mínima y metros de cable necesarios")
print("=" * 70)

arbol_min, total_metros_cable = kruskal(casa)
for orig, dest, metros in arbol_min:
    print(f"  {orig} --({metros} m)--> {dest}")

print(f"\n>> Total de metros de cable necesarios para conectar todos los ambientes: {total_metros_cable} metros.")


# ==============================================================================
# d. Determinar cuál es el camino más corto desde la habitación 1 hasta la
#    sala de estar para determinar cuántos metros de cable de red se necesitan
#    para conectar el router con el Smart Tv
# ==============================================================================
print("\n" + "=" * 70)
print("PUNTO D: Camino más corto desde 'habitación 1' hasta 'sala de estar'")
print("=" * 70)

pila_camino = dijkstra(casa, "habitación 1", "sala de estar")
camino, metros_red = recuperar_camino(pila_camino, "sala de estar")

print(f"  Camino más corto: {' -> '.join(camino)}")
print(f"  Metros de cable de red necesarios (Router a Smart TV): {metros_red} metros.")
