# 📚 Gestor de Notas Académicas

El "Gestor de Notas Académicas" es un sistema diseñado para facilitar el registro, consulta y administración de las calificaciones obtenidas por un estudiante a lo largo de sus cursos.

Su objetivo principal es brindar una herramienta sencilla pero funcional que permita llevar un control ordenado de las materias cursadas, las notas obtenidas y los promedios calculados. Este sistema está dirigido a cualquier persona que necesite organizar y centralizar su información académica para evaluar su rendimiento.

---

## 🎯 Requisitos del Sistema (Avance 01)

### 💻 Funcionalidades Implementadas (Avance 02)

| ID | Funcionalidad | Estado |
| :--- | :--- | :--- |
| **F1** | Registrar un nuevo curso y su nota. | **IMPLEMENTADO** |
| **F2** | Mostrar todas las notas registradas. | **IMPLEMENTADO** |
| **F3** | Calcular y mostrar el promedio general. | **IMPLEMENTADO** |
| F4 | Actualizar nota de un curso específico. | Pendiente (Avance 3) |
| F5 | Eliminar curso del registro. | Pendiente (Avance 4) |
| F6 | Ordenar notas (Burbuja / Inserción). | Pendiente (Avance 5) |

### ⚙️ Requisitos No Funcionales

* El sistema se ejecuta en **consola** utilizando el lenguaje **Python**.
* No se utilizan librerías externas.
* La lógica del menú principal utiliza **bucles** y **condicionales**.
* El diseño lógico inicial se realizó en **pseudocódigo** (`pseudocodigo.txt`).

---

## 🚀 Lógica Implementada en el Avance 02

El código (`Prototipo - Python.py`) implementa la siguiente lógica:

1.  **Estructura de Menú:** Uso de un bucle `MIENTRAS` para mantener el menú activo hasta que el usuario selecciona "Salir".
2.  **Estructura de Datos:** Se utilizan **listas paralelas** (`Cursos` y `Notas`) para almacenar la información de forma ordenada.
3.  **Registro y Validación:** Se captura el nombre del curso y la nota, validando que la nota sea un valor numérico y que esté dentro del rango permitido (0-100).
4.  **Cálculo de Promedio:** Se utiliza un bucle (`PARA`) para iterar sobre la lista de `Notas`, sumar los valores, y luego dividir por el número total de notas (`Contador` o `TAMAÑO(Lista)`).

