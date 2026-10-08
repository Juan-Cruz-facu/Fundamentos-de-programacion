# -*- coding: utf-8 -*-
"""
Ejercicio 16 - Cola de Impresión con Prioridades
"""

import heapq

class ColaImpresion:
    def __init__(self):
        self._cola = []
        self._contador = 0
        self._prioridades = {
            "empleado": 1,
            "staff_ti": 2,
            "gerente": 3
        }

    def cargar_documento(self, nombre, rol):
        prioridad = self._prioridades.get(rol.lower().replace(" ", "_"), 3)
        self._contador += 1
        # Se guarda (prioridad, contador, nombre, rol) para resolver empates en orden de llegada (FIFO)
        heapq.heappush(self._cola, (prioridad, self._contador, nombre, rol))
        print(f"  [Cargado] '{nombre}' ({rol})")

    def imprimir_documento(self):
        if not self._cola:
            print("  La cola está vacía.")
            return None
        prioridad, turno, nombre, rol = heapq.heappop(self._cola)
        print(f"  [Imprimiendo] '{nombre}' ({rol})")
        return nombre

    def imprimir_varios(self, cantidad):
        for _ in range(cantidad):
            if not self._cola:
                break
            self.imprimir_documento()

    def mostrar_estado(self):
        print(f"\n  === Documentos en espera ({len(self._cola)}) ===")
        if not self._cola:
            print("    Ninguno")
        for prioridad, turno, nombre, rol in sorted(self._cola):
            print(f"    - [{rol.upper()}] '{nombre}' (Orden: {turno})")
        print("  ============================================")

if __name__ == "__main__":
    cola = ColaImpresion()

    # 1. Cargar tres documentos de empleados
    print("1. Cargando tres documentos de empleados...")
    cola.cargar_documento("Reporte_Ventas.pdf", "empleado")
    cola.cargar_documento("Planilla_Horarios.xlsx", "empleado")
    cola.cargar_documento("Solicitud_Licencia.docx", "empleado")
    cola.mostrar_estado()

    # 2. Imprimir el primer documento de la cola
    print("\n2. Imprimiendo el primer documento...")
    cola.imprimir_documento()
    cola.mostrar_estado()

    # 3. Cargar dos documentos del staff de TI
    print("\n3. Cargando dos documentos de staff de TI...")
    cola.cargar_documento("Actualizacion_Servidores.txt", "staff_ti")
    cola.cargar_documento("Backup_BD.sql", "staff_ti")

    # 4. Cargar un documento del gerente
    print("\n4. Cargando un documento del gerente...")
    cola.cargar_documento("Plan_Estrategico.pptx", "gerente")
    cola.mostrar_estado()

    # 5. Imprimir los dos primeros documentos de la cola
    print("\n5. Imprimiendo los dos primeros documentos...")
    cola.imprimir_varios(2)
    cola.mostrar_estado()

    # 6. Cargar dos documentos de empleados y uno de gerente
    print("\n6. Cargando dos documentos de empleados y uno de gerente...")
    cola.cargar_documento("Gastos_Viaje.pdf", "empleado")
    cola.cargar_documento("Recibo_Sueldo.pdf", "empleado")
    cola.cargar_documento("Presupuesto_Anual.xlsx", "gerente")
    cola.mostrar_estado()

    # 7. Imprimir todos los documentos restantes en la cola
    print("\n7. Imprimiendo todos los documentos restantes...")
    cola.imprimir_varios(len(cola._cola))
    cola.mostrar_estado()
