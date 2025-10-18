# 📚 Gestor de Notas Académicas

El "Gestor de Notas Académicas" es un sistema diseñado para facilitar el registro, consulta y administración de las calificaciones obtenidas por un estudiante a lo largo de sus cursos.

Su objetivo principal es brindar una herramienta sencilla pero funcional que permita llevar un control ordenado de las materias cursadas, las notas obtenidas y los promedios calculados. Este sistema está dirigido a cualquier persona que necesite organizar y centralizar su información académica para evaluar su rendimiento.

---

## 🎯 Requisitos del Sistema (Avance 01)

### 💻 Funcionalidades Implementadas (Hasta Avance 05)

| ID | Funcionalidad | Estado |
| :--- | :--- | :--- |
| **F1** | Registrar un nuevo curso y su nota. | **IMPLEMENTADO** (Avance 2) |
| **F2** | Mostrar todas las notas registradas. | **IMPLEMENTADO** (Avance 2) |
| **F3** | Calcular y mostrar el promedio general. | **IMPLEMENTADO** (Avance 2) |
| **F4** | Actualizar nota de un curso específico. | **IMPLEMENTADO** (Avance 3) |
| **F5** | Eliminar curso del registro. | **IMPLEMENTADO** (Avance 4) |
| **F6** | Ordenar notas (Burbuja / Inserción). | **IMPLEMENTADO** (Avance 5) |

### ⚙️ Requisitos No Funcionales

* El sistema se ejecuta en **consola** utilizando el lenguaje **Python**.
* No se utilizan librerías externas.
* La lógica del menú principal utiliza **bucles** y **condicionales**.
* El código está **modularizado** en funciones (implementado en Avance 4).
* Se utilizan **Pilas (Stack)** y **Colas (Queue)** para estructuras de datos avanzadas (implementado en Avance 5).
* El diseño lógico se realizó en **pseudocódigo** (`pseudocodigo.txt`).

---

## 🚀 Lógica Implementada (Avances 02, 03, 04 y 05)

El código (`Prototipo - Python.py`) implementa la gestión de datos, utilizando **listas paralelas** (`cursos` y `notas`) para mantener la información asociada.

### Avance 05: Estructuras Avanzadas y Ordenamiento

#### 1. Estructuras de Datos (Pila y Cola)
* **Pila (Historial de Acciones):** Se utiliza una lista para simular una estructura **LIFO** (Last-In, First-Out). Cada acción importante (registro, actualización, eliminación, ordenamiento) se "apila" (`.append()`) en el `Historial_Pila`. Esto permite auditar las últimas operaciones realizadas.
* **Cola (Lista de Revisión):** (Se debe incluir si se implementó en Python. Si no, ajustar la descripción). Se puede usar una lista para simular la estructura **FIFO** (First-In, First-Out) para una lista de cursos pendientes de revisión.

#### 2. Algoritmos de Ordenamiento
Se implementaron dos funciones para ordenar los datos:
* **Ordenamiento por Burbuja (Bubble Sort):** Un algoritmo simple que compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto, repitiendo el proceso hasta que toda la lista esté ordenada.
* **Ordenamiento por Inserción (Insertion Sort):** Un algoritmo que construye la lista ordenada final un elemento a la vez, insertando cada nuevo elemento en la posición correcta dentro de la sublista ya ordenada.
* **Asociación de Datos:** En ambos algoritmos, cada vez que se intercambian dos notas, se realiza un intercambio simultáneo en la lista de `cursos` para garantizar que la nota y el curso permanezcan correctamente asociados.

### Avances Anteriores

* **Avance 04 (Modularización y Eliminación):** El código fue dividido en funciones (`def`) para cada operación (Registrar, Actualizar, Eliminar). Se implementó la **Eliminación de Datos** utilizando la Búsqueda Lineal para encontrar el índice y el método `.pop()` para remover el curso y la nota.
* **Avance 03 (Actualización):** Se implementó la función de **Actualizar Datos** usando un bucle (`PARA` o `MIENTRAS`) para realizar una **Búsqueda Lineal** por el nombre del curso.
* **Avance 02 (Base):** Implementación de **Registro**, **Visualización** y **Cálculo de Promedio**, incluyendo validación de notas (0-100).
