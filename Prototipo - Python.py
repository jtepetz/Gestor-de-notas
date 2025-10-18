# -----------------------------------------------------
# GESTOR DE NOTAS ACADÉMICAS - IMPLEMENTACIÓN COMPLETA
# Cumple con Avances 1, 2, 3, 4 y 5
# -----------------------------------------------------

# Variables Globales (Estructuras de datos)
cursos = []      # Lista para nombres de cursos
notas = []       # Lista para notas asociadas
historial_pila = [] # Pila (LIFO) para registrar acciones

# =====================================================
# FUNCIONES DE AYUDA Y ESTRUCTURAS DE DATOS (Avance 5)
# =====================================================

def apilar_accion(pila, accion):
    """Simula la operación PUSH (APILAR) para el historial."""
    pila.append(accion)

# =====================================================
# FUNCIONES CRUD Y PROMEDIO (Avances 2, 3 y 4)
# =====================================================

def registrar_nota(cursos, notas, pila): # Avance 2
    """Registra un nuevo curso y nota."""
    print("\n--- Registrar Curso ---")
    nombre_curso = input("Nombre del curso: ")
    try:
        nueva_nota = float(input("Nota (0-100): "))
        if 0 <= nueva_nota <= 100:
            cursos.append(nombre_curso)
            notas.append(nueva_nota)
            print(f"Curso '{nombre_curso}' registrado.")
            apilar_accion(pila, f"Registró {nombre_curso}")
        else:
            print("Error: La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Error: La nota debe ser un valor numérico.")

def mostrar_notas(cursos, notas): # Avance 2
    """Muestra todos los cursos y sus notas."""
    print("\n--- Cursos Registrados ---")
    if not cursos:
        print("No hay cursos registrados.")
        return
    for curso, nota in zip(cursos, notas):
        print(f"Curso: {curso} - Nota: {nota}")

def calcular_promedio(notas): # Avance 2
    """Calcula y muestra el promedio general."""
    if not notas:
        print("No hay notas para calcular promedio.")
        return
    promedio = sum(notas) / len(notas)
    print(f"\n--- Promedio General ---")
    print(f"El promedio general es: {promedio:.2f}")

def actualizar_nota(cursos, notas, pila): # Avance 3 (Búsqueda Lineal y Actualización)
    """Busca un curso y permite actualizar su nota."""
    print("\n--- Actualizar Nota ---")
    nombre_a_buscar = input("Ingrese el nombre del curso a actualizar: ")
    
    encontrado = False
    for i, curso in enumerate(cursos): # Búsqueda Lineal
        if curso == nombre_a_buscar:
            print(f"Curso encontrado. Nota actual: {notas[i]}")
            try:
                nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                if 0 <= nueva_nota <= 100:
                    notas[i] = nueva_nota # Actualización de datos
                    print(f"Nota de '{nombre_a_buscar}' actualizada a {nueva_nota}.")
                    apilar_accion(pila, f"Actualizó nota de {nombre_a_buscar}")
                else:
                    print("Error: La nota ingresada no es válida.")
            except ValueError:
                print("Error: La nota debe ser un valor numérico.")
            encontrado = True
            break
            
    if not encontrado:
        print(f"Error: El curso '{nombre_a_buscar}' no fue encontrado.")

def eliminar_curso(cursos, notas, pila): # Avance 4 (Eliminación)
    """Busca un curso y lo elimina del registro."""
    print("\n--- Eliminar Curso ---")
    nombre_a_eliminar = input("Ingrese el nombre del curso a eliminar: ")
    
    encontrado = False
    for i, curso in enumerate(cursos):
        if curso == nombre_a_eliminar:
            # Eliminación de las dos listas en el mismo índice
            cursos.pop(i)
            notas.pop(i)
            print(f"El curso '{nombre_a_eliminar}' ha sido eliminado exitosamente.")
            apilar_accion(pila, f"Eliminó {nombre_a_eliminar}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"Error: El curso '{nombre_a_eliminar}' no fue encontrado.")

# =====================================================
# FUNCIONES DE ORDENAMIENTO (Avance 5)
# =====================================================

def ordenar_burbuja(cursos, notas, pila):
    """Implementa el algoritmo de Ordenamiento por Burbuja."""
    n = len(notas)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if notas[j] > notas[j + 1]: # Comparación de notas
                # Intercambio de NOTAS
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
                # Intercambio de CURSOS (para mantener la asociación)
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    print("\nNotas ordenadas (ascendente) por Burbuja.")
    apilar_accion(pila, "Ordenó por Burbuja")

def ordenar_insercion(cursos, notas, pila):
    """Implementa el algoritmo de Ordenamiento por Inserción."""
    n = len(notas)
    for i in range(1, n):
        clave_nota = notas[i]
        clave_curso = cursos[i]
        j = i - 1
        
        while j >= 0 and notas[j] > clave_nota:
            notas[j + 1] = notas[j]
            cursos[j + 1] = cursos[j]
            j -= 1
        notas[j + 1] = clave_nota
        cursos[j + 1] = clave_curso
    print("\nNotas ordenadas (ascendente) por Inserción.")
    apilar_accion(pila, "Ordenó por Inserción")

# =====================================================
# MENÚ PRINCIPAL
# =====================================================

def menu_principal():
    """Bucle principal del programa."""
    opcion = 0
    
    apilar_accion(historial_pila, "Inicio del sistema.")
    
    while opcion != 8:
        print("\n===================================")
        print("     GESTOR DE NOTAS ACADÉMICAS")
        print("===================================")
        print("1. Registrar nuevo curso y nota")
        print("2. Mostrar todas las notas")
        print("3. Calcular promedio general")
        print("4. Actualizar nota de curso")
        print("5. Eliminar curso")
        print("6. Ordenar notas (Burbuja)")
        print("7. Ordenar notas (Inserción)")
        print("8. Salir")
        print("-----------------------------------")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                registrar_nota(cursos, notas, historial_pila)
            elif opcion == 2:
                mostrar_notas(cursos, notas)
            elif opcion == 3:
                calcular_promedio(notas)
            elif opcion == 4:
                actualizar_nota(cursos, notas, historial_pila)
            elif opcion == 5:
                eliminar_curso(cursos, notas, historial_pila)
            elif opcion == 6:
                ordenar_burbuja(cursos, notas, historial_pila)
            elif opcion == 7:
                ordenar_insercion(cursos, notas, historial_pila)
            elif opcion == 8:
                print("\nSaliendo del sistema...")
                print("Historial de las últimas acciones (Pila):")
                # Muestra la pila, la última acción está al final
                for accion in reversed(historial_pila):
                    print(f"- {accion}")
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Ejecución del programa
if __name__ == "__main__":
    menu_principal()
