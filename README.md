# 📚 Gestor de Notas Académicas

El "Gestor de Notas Académicas" es un sistema de consola diseñado para facilitar el registro, consulta, modificación y administración de calificaciones. Su objetivo es proporcionar una herramienta sencilla y funcional para que estudiantes o académicos lleven un control ordenado de sus cursos, notas y rendimiento general.

Este prototipo implementa diversas estructuras de datos y algoritmos fundamentales para demostrar la capacidad de gestión de información en un entorno básico.

---

## 🎯 Requisitos del Sistema (Estado Final)

### 💻 Funcionalidades Implementadas (Avances 1-5)

| ID | Funcionalidad | Estado | Descripción |
| :--- | :--- | :--- | :--- |
| **F1** | Registrar nuevo curso y nota. | **IMPLEMENTADO** | Añade nuevos registros a las listas paralelas. |
| **F2** | Mostrar todas las notas. | **IMPLEMENTADO** | Muestra el contenido actual de las listas. |
| **F3** | Calcular promedio general. | **IMPLEMENTADO** | Suma de notas dividido por el total de cursos. |
| **F4** | Actualizar nota de curso. | **IMPLEMENTADO** | Utiliza Búsqueda Lineal para modificar un registro existente. |
| **F5** | Eliminar curso. | **IMPLEMENTADO** | Utiliza Búsqueda Lineal para remover datos sincronizadamente. |
| **F6** | Ordenar notas (Burbuja / Inserción). | **IMPLEMENTADO** | Implementación de dos algoritmos de complejidad O(n²) con intercambio paralelo de datos. |
| **F7** | Mostrar Historial (Pila). | **IMPLEMENTADO** | Usa una estructura LIFO para auditar las últimas acciones. |

### ⚙️ Requisitos No Funcionales

* El sistema se ejecuta en **consola** utilizando el lenguaje **Python**.
* No se utilizan librerías externas o frameworks.
* El código está completamente **modularizado** en funciones (subrutinas).
* Se emplean **listas paralelas**, **Pilas (LIFO)** y **Búsqueda Lineal**.
* El diseño lógico completo se encuentra en el archivo **`pseudocodigo.txt`**.

---

## 🚀 Lógica Implementada (Resumen Técnico)

El código final (`Prototipo - Python.py`) se basa en los siguientes principios:

1.  **Estructura de Datos:** Uso de **Listas Paralelas** (`cursos` y `notas`) para mantener la asociación, y una **Pila** (`historial_pila`) implementada con la lógica LIFO (Last-In, First-Out) para el registro de acciones.
2.  **Búsqueda:** Todas las operaciones de modificación/eliminación (F4, F5) se basan en la **Búsqueda Lineal** (`enumerate` en Python) para obtener el índice preciso del elemento.
3.  **Algoritmos de Ordenamiento:** Se implementaron los algoritmos **Burbuja** e **Inserción** para ordenar la lista de notas. Ambos garantizan el **intercambio paralelo** de datos entre `cursos` y `notas` en cada operación de *swap*, manteniendo la complejidad de tiempo en **O(n²)**.
