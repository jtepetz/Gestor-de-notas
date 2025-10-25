# ============================================================
# GESTOR DE NOTAS ACADÉMICAS - Versión Final
# Autor: Joshua JC
# Fecha: Octubre 2025
# Descripción: Sistema en consola para registrar, gestionar y analizar notas académicas.
# ============================================================

# ---------------------------
# VARIABLES GLOBALES
# ---------------------------
cursos = []  # Lista principal de cursos (cada curso será un diccionario con 'nombre' y 'nota')
historial_cambios = []  # Pila para registrar eliminaciones o actualizaciones
cola_revision = []  # Cola para simular solicitudes de revisión

# ---------------------------
# FUNCIONES PRINCIPALES
# ---------------------------

def registrar_curso():
    """Permite registrar un curso y su nota, validando los datos."""
    nombre = input("Ingrese el nombre del curso: ").strip()
    if not nombre:
        print("⚠️ El nombre no puede estar vacío.")
        return

    # Evitar duplicados
    for curso in cursos:
        if curso["nombre"].lower() == nombre.lower():
            print("⚠️ El curso ya está registrado.")
            return

    try:
        nota = float(input("Ingrese la nota obtenida (0-100): "))
        if nota < 0 or nota > 100:
            print("⚠️ La nota debe estar entre 0 y 100.")
            return
    except ValueError:
        print("⚠️ Ingrese un valor numérico válido.")
        return

    cursos.append({"nombre": nombre, "nota": nota})
    print(f"✅ Curso '{nombre}' registrado con éxito.")


def mostrar_cursos():
    """Muestra todos los cursos registrados."""
    if not cursos:
        print("📭 No hay cursos registrados.")
        return

    print("\n📚 Cursos registrados:")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']}")


def calcular_promedio():
    """Calcula y muestra el promedio general de las notas."""
    if not cursos:
        print("⚠️ No hay cursos registrados para calcular el promedio.")
        return

    promedio = sum(c["nota"] for c in cursos) / len(cursos)
    print(f"📊 Promedio general: {promedio:.2f}")


def contar_aprobados_reprobados():
    """Cuenta cuántos cursos están aprobados (>=60) y reprobados."""
    if not cursos:
        print("⚠️ No hay cursos registrados.")
        return

    aprobados = sum(1 for c in cursos if c["nota"] >= 60)
    reprobados = len(cursos) - aprobados
    print(f"✅ Cursos aprobados: {aprobados}")
    print(f"❌ Cursos reprobados: {reprobados}")


def buscar_curso_lineal(nombre):
    """Realiza búsqueda lineal de un curso por nombre."""
    for curso in cursos:
        if nombre.lower() in curso["nombre"].lower():
            print(f"🔎 Curso encontrado: {curso['nombre']} - Nota: {curso['nota']}")
            return
    print("⚠️ No se encontró el curso.")


def actualizar_nota():
    """Permite actualizar la nota de un curso existente."""
    nombre = input("Ingrese el nombre del curso a actualizar: ").strip()
    for curso in cursos:
        if curso["nombre"].lower() == nombre.lower():
            try:
                nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print("⚠️ La nota debe estar entre 0 y 100.")
                    return
            except ValueError:
                print("⚠️ Ingrese un número válido.")
                return

            historial_cambios.append(f"Se actualizó: {curso['nombre']} - Nota anterior: {curso['nota']} → Nueva nota: {nueva_nota}")
            curso["nota"] = nueva_nota
            print("✅ Nota actualizada correctamente.")
            return

    print("⚠️ No se encontró el curso.")


def eliminar_curso():
    """Elimina un curso de la lista, con confirmación."""
    nombre = input("Ingrese el nombre del curso a eliminar: ").strip()
    for curso in cursos:
        if curso["nombre"].lower() == nombre.lower():
            confirm = input(f"¿Está seguro de eliminar '{nombre}'? (s/n): ").lower()
            if confirm == "s":
                historial_cambios.append(f"Se eliminó: {curso['nombre']} - Nota: {curso['nota']}")
                cursos.remove(curso)
                print("🗑️ Curso eliminado correctamente.")
            else:
                print("❎ Operación cancelada.")
            return
    print("⚠️ No se encontró el curso.")


def ordenar_por_nota():
    """Ordena los cursos por nota (descendente) usando el método burbuja."""
    n = len(cursos)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if cursos[j]["nota"] < cursos[j + 1]["nota"]:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    print("📈 Cursos ordenados por nota (descendente):")
    mostrar_cursos()


def ordenar_por_nombre():
    """Ordena los cursos alfabéticamente por nombre usando inserción."""
    for i in range(1, len(cursos)):
        actual = cursos[i]
        j = i - 1
        while j >= 0 and cursos[j]["nombre"].lower() > actual["nombre"].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = actual
    print("🔤 Cursos ordenados alfabéticamente:")
    mostrar_cursos()


def buscar_curso_binaria(nombre):
    """Realiza búsqueda binaria en la lista ordenada por nombre."""
    if not cursos:
        print("⚠️ No hay cursos registrados.")
        return

    # Asegurar que la lista esté ordenada por nombre
    ordenar_por_nombre()

    inicio, fin = 0, len(cursos) - 1
    nombre = nombre.lower()

    while inicio <= fin:
        medio = (inicio + fin) // 2
        actual = cursos[medio]["nombre"].lower()

        if actual == nombre:
            print(f"🔍 Curso encontrado: {cursos[medio]['nombre']} - Nota: {cursos[medio]['nota']}")
            return
        elif actual < nombre:
            inicio = medio + 1
        else:
            fin = medio - 1

    print("⚠️ Curso no encontrado.")


def simular_cola_revision():
    """Simula una cola de solicitudes de revisión."""
    print("Ingrese los cursos a enviar a revisión (escriba 'fin' para terminar):")
    while True:
        curso = input("> ").strip()
        if curso.lower() == "fin":
            break
        cola_revision.append(curso)

    if not cola_revision:
        print("⚠️ No se agregaron solicitudes de revisión.")
        return

    print("\nProcesando solicitudes de revisión:")
    while cola_revision:
        curso = cola_revision.pop(0)  # FIFO
        print(f"🔁 Revisando: {curso}")
    print("✅ Todas las solicitudes fueron procesadas.")


def mostrar_historial():
    """Muestra los últimos cambios realizados (pila LIFO)."""
    if not historial_cambios:
        print("📭 No hay historial de cambios.")
        return

    print("🕘 Historial de cambios recientes:")
    for i, cambio in enumerate(reversed(historial_cambios), 1):
        print(f"{i}. {cambio}")


# ---------------------------
# MENÚ PRINCIPAL
# ---------------------------
def menu():
    while True:
        print("\n====== GESTOR DE NOTAS ACADÉMICAS ======")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre (búsqueda lineal)")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar un curso")
        print("8. Ordenar cursos por nota (burbuja)")
        print("9. Ordenar cursos por nombre (inserción)")
        print("10. Buscar curso por nombre (búsqueda binaria)")
        print("11. Simular cola de solicitudes de revisión")
        print("12. Mostrar historial de cambios (pila)")
        print("13. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1": registrar_curso()
        elif opcion == "2": mostrar_cursos()
        elif opcion == "3": calcular_promedio()
        elif opcion == "4": contar_aprobados_reprobados()
        elif opcion == "5": buscar_curso_lineal(input("Ingrese el nombre del curso: "))
        elif opcion == "6": actualizar_nota()
        elif opcion == "7": eliminar_curso()
        elif opcion == "8": ordenar_por_nota()
        elif opcion == "9": ordenar_por_nombre()
        elif opcion == "10": buscar_curso_binaria(input("Ingrese el nombre del curso a buscar: "))
        elif opcion == "11": simular_cola_revision()
        elif opcion == "12": mostrar_historial()
        elif opcion == "13":
            print("👋 Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")


# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------
if __name__ == "__main__":
    menu()

