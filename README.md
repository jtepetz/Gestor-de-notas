# 📚 Gestor de Notas Académicas

El "Gestor de Notas Académicas" es un sistema diseñado para facilitar el registro, consulta y administración de las calificaciones obtenidas por un estudiante a lo largo de sus cursos.

Su objetivo principal es brindar una herramienta sencilla pero funcional que permita llevar un control ordenado de las materias cursadas, las notas obtenidas y los promedios calculados. Este sistema está dirigido a cualquier persona que necesite organizar y centralizar su información académica para evaluar su rendimiento.

---

## 🎯 Requisitos del Sistema (Avance 01)

### 💻 Funcionalidades Implementadas (Hasta Avance 03)

| ID | Funcionalidad | Estado |
| :--- | :--- | :--- |
| **F1** | Registrar un nuevo curso y su nota. | **IMPLEMENTADO** (Avance 2) |
| **F2** | Mostrar todas las notas registradas. | **IMPLEMENTADO** (Avance 2) |
| **F3** | Calcular y mostrar el promedio general. | **IMPLEMENTADO** (Avance 2) |
| **F4** | Actualizar nota de un curso específico. | **IMPLEMENTADO** (Avance 3) |
| F5 | Eliminar curso del registro. | Pendiente (Avance 4) |
| F6 | Ordenar notas (Burbuja / Inserción). | Pendiente (Avance 5) |

### ⚙️ Requisitos No Funcionales

* El sistema se ejecuta en **consola** utilizando el lenguaje **Python**.
* No se utilizan librerías externas.
* La lógica del menú principal utiliza **bucles** y **condicionales**.
* El diseño lógico inicial se realizó en **pseudocódigo** (`pseudocodigo.txt`).

---

## 🚀 Lógica Implementada (Avances 02 y 03)

El código (`Prototipo - Python.py`) implementa la lógica de gestión de datos, utilizando **listas paralelas** (`cursos` y `notas`) para mantener la información asociada.

### Avance 02: Registro y Promedio
* **Listas y Bucles:** Se utiliza un bucle `MIENTRAS` para el menú principal y bucles `PARA` para recorrer las listas y calcular el promedio.
* **Validación:** Se valida que las notas ingresadas estén en el rango de 0 a 100.

### Avance 03: Búsqueda y Actualización (Búsqueda Lineal)
* **Búsqueda Lineal:** Se implementa un bucle (`PARA` o `MIENTRAS`) dentro de la función de actualización. Este bucle recorre secuencialmente la lista de `cursos` (desde el índice 0 hasta N-1) buscando una coincidencia exacta con el nombre ingresado por el usuario.
* **Contadores y Condicionales:** Al encontrar el curso (usando un **condicional** `SI`), se utiliza el **índice** (`i`) del contador del bucle para acceder y modificar la nota correspondiente en la lista `notas` (`notas[i] = nueva_nota`).
