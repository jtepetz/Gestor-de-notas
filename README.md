# 📚 Gestor de Notas Académicas

El "Gestor de Notas Académicas" es un sistema diseñado para facilitar el registro, consulta y administración de las calificaciones obtenidas por un estudiante a lo largo de sus cursos.

Su objetivo principal es brindar una herramienta sencilla pero funcional que permita llevar un control ordenado de las materias cursadas, las notas obtenidas y los promedios calculados. Este sistema está dirigido a cualquier persona que necesite organizar y centralizar su información académica para evaluar su rendimiento.

---

## 🎯 Requisitos del Sistema (Avance 01)

### 💻 Funcionalidades Implementadas (Hasta Avance 04)

| ID | Funcionalidad | Estado |
| :--- | :--- | :--- |
| **F1** | Registrar un nuevo curso y su nota. | **IMPLEMENTADO** (Avance 2) |
| **F2** | Mostrar todas las notas registradas. | **IMPLEMENTADO** (Avance 2) |
| **F3** | Calcular y mostrar el promedio general. | **IMPLEMENTADO** (Avance 2) |
| **F4** | Actualizar nota de un curso específico. | **IMPLEMENTADO** (Avance 3) |
| **F5** | Eliminar curso del registro. | **IMPLEMENTADO** (Avance 4) |
| F6 | Ordenar notas (Burbuja / Inserción). | Pendiente (Avance 5) |

### ⚙️ Requisitos No Funcionales

* El sistema se ejecuta en **consola** utilizando el lenguaje **Python**.
* No se utilizan librerías externas.
* La lógica del menú principal utiliza **bucles** y **condicionales**.
* El código está **modularizado** en funciones (implementado en Avance 4).
* El diseño lógico se realizó en **pseudocódigo** (`pseudocodigo.txt`).

---

## 🚀 Lógica Implementada (Avances 02, 03 y 04)

El código (`Prototipo - Python.py`) implementa la gestión de datos, utilizando **listas paralelas** (`cursos` y `notas`) para mantener la información asociada.

### Avance 04: Modularización y Eliminación de Datos

#### 1. Modularización con Funciones
Todo el código ha sido **modularizado** utilizando la estructura `def` en Python (subrutinas en pseudocódigo). Esto mejora la organización, legibilidad y reutilización del código, separando la lógica del menú de la lógica de las operaciones (CRUD).

#### 2. Eliminación de Datos (Búsqueda Lineal)
* **Proceso:** La función de eliminación realiza primero una **Búsqueda Lineal** (misma lógica que en el Avance 3) para encontrar la posición (índice) del curso que el usuario desea borrar.
* **Acción:** Una vez encontrado el índice, se utiliza el método nativo del lenguaje (`.pop()` o `del`) para **remover el elemento de la lista de cursos y la lista de notas** en esa posición específica, asegurando que los datos queden sincronizados.

### Avances Anteriores
* **Avance 03:** Implementación de la **Actualización de Datos** utilizando un bucle para la **Búsqueda Lineal**.
* **Avance 02:** Implementación de **Registro**, **Visualización** y **Cálculo de Promedio**, incluyendo validación de notas.
