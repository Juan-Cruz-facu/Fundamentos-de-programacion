from tda_grafo import (
    Grafo,
    insertar_vertice,
    insertar_arista,
    buscar_vertice,
    eliminar_arista_grafo,
    marcar_no_visitado,
    barrido_profundidad,
    barrido_amplitud,
    dijkstra,
    recuperar_camino,
    kruskal,
)

# h. Debe utilizar un grafo no dirigido
red = Grafo(dirigido=False)

# a. Cada nodo además del nombre del equipo deberá almacenar su tipo:
# pc, notebook, servidor, router, switch, impresora
equipos = [
    ("Red Hat", "notebook"),
    ("Debian", "notebook"),
    ("Arch", "notebook"),
    ("Manjaro", "pc"),
    ("Parrot", "pc"),
    ("Fedora", "pc"),
    ("Ubuntu", "pc"),
    ("Mint", "pc"),
    ("Guaraní", "servidor"),
    ("MongoDB", "servidor"),
    ("Switch 1", "switch"),
    ("Switch 2", "switch"),
    ("Router 1", "router"),
    ("Router 2", "router"),
    ("Router 3", "router"),
    ("Impresora", "impresora"),
]

for nombre, tipo in equipos:
    insertar_vertice(red, nombre, datos_extra=tipo)

# Carga de conexiones (aristas con sus pesos según la figura del libro)
conexiones = [
    # Conexiones de Switch 1
    ("Switch 1", "Debian", 17),
    ("Switch 1", "Ubuntu", 18),
    ("Switch 1", "Impresora", 22),
    ("Switch 1", "Mint", 80),
    ("Switch 1", "Router 1", 29),
    # Conexiones de Router 1, Router 2 y Router 3
    ("Router 1", "Router 2", 37),
    ("Router 1", "Router 3", 43),
    ("Router 2", "Router 3", 50),
    # Conexiones de Router 2
    ("Router 2", "Red Hat", 25),
    ("Router 2", "Guaraní", 9),
    # Conexiones de Router 3
    ("Router 3", "Switch 2", 61),
    # Conexiones de Switch 2
    ("Switch 2", "Manjaro", 40),
    ("Switch 2", "Parrot", 12),
    ("Switch 2", "MongoDB", 5),
    ("Switch 2", "Arch", 56),
    ("Switch 2", "Fedora", 3),
]

for orig, dest, peso in conexiones:
    v_orig = buscar_vertice(red, orig)
    v_dest = buscar_vertice(red, dest)
    insertar_arista(red, peso, v_orig, v_dest)


# ==============================================================================
# b. Realizar un barrido en profundidad y amplitud partiendo desde las tres
#    notebook: Red Hat, Debian, Arch
# ==============================================================================
print("=" * 70)
print("PUNTO B: Barridos en profundidad y amplitud desde las 3 notebooks")
print("=" * 70)

notebooks = ["Red Hat", "Debian", "Arch"]
for nb in notebooks:
    vertice_nb = buscar_vertice(red, nb)
    print(f"\n--- Barrido en PROFUNDIDAD desde {nb} ({vertice_nb.datos_extra}) ---")
    marcar_no_visitado(red)
    barrido_profundidad(red, vertice_nb)

    print(f"\n--- Barrido en AMPLITUD desde {nb} ({vertice_nb.datos_extra}) ---")
    marcar_no_visitado(red)
    barrido_amplitud(red, vertice_nb)


# ==============================================================================
# c. Encontrar el camino más corto para enviar a imprimir un documento desde
#    la pc: Manjaro, Red Hat, Fedora hasta la impresora
# ==============================================================================
print("\n" + "=" * 70)
print("PUNTO C: Camino más corto para imprimir desde Manjaro, Red Hat y Fedora")
print("=" * 70)

equipos_impresion = ["Manjaro", "Red Hat", "Fedora"]
for eq in equipos_impresion:
    pila_camino = dijkstra(red, eq, "Impresora")
    camino, costo = recuperar_camino(pila_camino, "Impresora")
    print(f"Desde {eq} hasta Impresora:")
    print(f"  Camino: {' -> '.join(camino)} | Costo total: {costo}")


# ==============================================================================
# d. Encontrar el árbol de expansión mínima
# ==============================================================================
print("\n" + "=" * 70)
print("PUNTO D: Árbol de expansión mínima (Kruskal)")
print("=" * 70)

arbol_min, peso_min = kruskal(red)
for orig, dest, peso in arbol_min:
    print(f"  {orig} --({peso})--> {dest}")
print(f"Peso total del árbol de expansión mínima: {peso_min}")


# ==============================================================================
# e. Determinar desde qué pc (no notebook) es el camino más corto hasta el
#    servidor "Guaraní"
# ==============================================================================
print("\n" + "=" * 70)
print("PUNTO E: PC (no notebook) con el camino más corto hasta el servidor 'Guaraní'")
print("=" * 70)

mejor_pc_guarani = None
menor_costo_guarani = float("inf")
mejor_camino_guarani = []

aux = red.inicio
while aux is not None:
    if aux.datos_extra == "pc":
        pila_camino = dijkstra(red, aux.info, "Guaraní")
        camino, costo = recuperar_camino(pila_camino, "Guaraní")
        print(f"  PC {aux.info} -> Guaraní: {' -> '.join(camino)} (Costo: {costo})")
        if costo < menor_costo_guarani:
            menor_costo_guarani = costo
            mejor_pc_guarani = aux.info
            mejor_camino_guarani = camino
    aux = aux.sig

print(f"\n>> Resultado: El camino más corto desde una PC a 'Guaraní' es desde '{mejor_pc_guarani}'")
print(f"   Camino: {' -> '.join(mejor_camino_guarani)} | Costo mínimo: {menor_costo_guarani}")


# ==============================================================================
# f. Indicar desde qué computadora del switch 01 es el camino más corto al
#    servidor "MongoDB"
# ==============================================================================
print("\n" + "=" * 70)
print("PUNTO F: Computadora conectada al Switch 1 con camino más corto a 'MongoDB'")
print("=" * 70)

v_switch1 = buscar_vertice(red, "Switch 1")
ady = v_switch1.adyacentes.inicio

mejor_comp_mongo = None
menor_costo_mongo = float("inf")
mejor_camino_mongo = []

while ady is not None:
    v_vecino = buscar_vertice(red, ady.destino)
    if v_vecino.datos_extra in ["pc", "notebook"]:
        pila_camino = dijkstra(red, v_vecino.info, "MongoDB")
        camino, costo = recuperar_camino(pila_camino, "MongoDB")
        print(f"  {v_vecino.info} ({v_vecino.datos_extra}) -> MongoDB: {' -> '.join(camino)} (Costo: {costo})")
        if costo < menor_costo_mongo:
            menor_costo_mongo = costo
            mejor_comp_mongo = v_vecino.info
            mejor_camino_mongo = camino
    ady = ady.sig

print(f"\n>> Resultado: La computadora del Switch 1 con camino más corto a 'MongoDB' es '{mejor_comp_mongo}'")
print(f"   Camino: {' -> '.join(mejor_camino_mongo)} | Costo mínimo: {menor_costo_mongo}")


# ==============================================================================
# g. Cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b
# ==============================================================================
print("\n" + "=" * 70)
print("PUNTO G: Cambiar conexión de la Impresora al Router 2 y volver a resolver")
print("=" * 70)

v_impresora = buscar_vertice(red, "Impresora")
v_router2 = buscar_vertice(red, "Router 2")

# Eliminamos la arista entre Switch 1 e Impresora (conservando su peso de 22)
peso_imp = eliminar_arista_grafo(red, v_switch1, v_impresora)
# Conectamos la Impresora al Router 2
insertar_arista(red, peso_imp, v_router2, v_impresora)
print(f"Se desconectó 'Impresora' de 'Switch 1' y se conectó a 'Router 2' (peso {peso_imp}).")

# Resolución del punto b nuevamente como pide el enunciado:
for nb in notebooks:
    vertice_nb = buscar_vertice(red, nb)
    print(f"\n--- [Nuevo] Barrido en PROFUNDIDAD desde {nb} ---")
    marcar_no_visitado(red)
    barrido_profundidad(red, vertice_nb)

    print(f"\n--- [Nuevo] Barrido en AMPLITUD desde {nb} ---")
    marcar_no_visitado(red)
    barrido_amplitud(red, vertice_nb)

# Adicionalmente mostramos cómo quedan los caminos de impresión (punto c) tras mover la impresora:
print("\n--- [Verificación extra] Nuevos caminos más cortos a la Impresora en Router 2 ---")
for eq in equipos_impresion:
    pila_camino = dijkstra(red, eq, "Impresora")
    camino, costo = recuperar_camino(pila_camino, "Impresora")
    print(f"Desde {eq} hasta Impresora: {' -> '.join(camino)} | Costo total: {costo}")
