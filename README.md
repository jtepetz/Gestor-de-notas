# 🎓 Gestor de Notas Académicas

---

## 📘 Descripción del proyecto
El **Gestor de Notas Académicas** es un sistema desarrollado en **Python** que permite a los estudiantes registrar, analizar y organizar sus calificaciones de forma sencilla desde la consola.

Su objetivo principal es facilitar el control del rendimiento académico mediante un menú interactivo que ofrece distintas operaciones, como registrar cursos, calcular promedios, ordenar notas, realizar búsquedas y simular estructuras de datos como **pilas y colas**.

Este proyecto se desarrolló como parte del curso de Programación, aplicando los principios de modularidad, validaciones básicas y estructuras de datos lineales.

---

## 🎯 Objetivos del sistema
* Brindar una herramienta práctica para gestionar las calificaciones de distintos cursos.
* Aplicar los conceptos de **listas, pilas, colas, búsqueda y ordenamiento** en un contexto funcional.
* Fomentar el diseño estructurado y el uso de **funciones modulares** en Python.
* Reforzar el pensamiento lógico a través de la implementación de algoritmos clásicos.

---

## ⚙️ Funcionalidades principales
1.  Registrar nuevo curso y nota
2.  Mostrar todos los cursos y notas
3.  Calcular promedio general
4.  Contar cursos aprobados y reprobados
5.  Buscar curso por nombre (búsqueda lineal)
6.  Actualizar nota de un curso
7.  Eliminar un curso
8.  Ordenar cursos por nota (burbuja)
9.  Ordenar cursos por nombre (inserción)
10. Buscar curso por nombre (búsqueda binaria)
11. Simular cola de solicitudes de revisión
12. Mostrar historial de cambios (pila)
13. Salir del sistema

---

## 🧠 Estructuras de datos utilizadas
* **Lista principal (`cursos`)** → almacena los cursos y sus notas.
* **Pila (`historial_cambios`)** → guarda los cambios en orden inverso (LIFO - *Last In, First Out*).
* **Cola (`cola_revision`)** → simula las solicitudes de revisión (FIFO - *First In, First Out*).

---

## 🧩 Algoritmos implementados
* **Ordenamiento burbuja** → para ordenar los cursos por nota (descendente).
* **Ordenamiento por inserción** → para ordenar los cursos alfabéticamente.
* **Búsqueda lineal** → para encontrar coincidencias parciales en nombres de cursos.
* **Búsqueda binaria** → para búsqueda exacta en lista ordenada.

---

## 💻 Requisitos del sistema
* **Lenguaje:** Python 3.8 o superior
* **Modo de ejecución:** Consola o terminal
* **Librerías externas:** Ninguna (solo funciones nativas de Python)
* **Sistema operativo:** Compatible con Windows, Linux y macOS

---

## ▶️ Instrucciones de ejecución
1.  Descarga o clona el repositorio desde GitHub:
    ```bash
    git clone [https://github.com/jtepetz/Gestor-de-notas.git](https://github.com/jtepetz/Gestor-de-notas.git)
    ```
2.  Abre la carpeta del proyecto:
    ```bash
    cd Gestor-de-notas
    ```
3.  Ejecuta el programa desde la consola:
    ```bash
    python gestor_notas.py
    ```
4.  Usa el menú interactivo para navegar entre las opciones.

---

## 🧾 Estructura del repositorio

GestorNotas/
├── gestor_notas.py           # Código fuente principal del sistema
├── pseudocodigo.txt          # Pseudocódigo general del programa
├── README.md                 # Descripción y reflexión personal
├── manual_tecnico.pdf        # Manual técnico del sistema
├── manual_usuario.pdf        # Manual de uso del sistema
└── evidencia/                # Capturas de ejecución (opcional)

---

### 📚 Documentación complementaria

* **Manual Técnico:** [Ver Manual Técnico Completo (PDF)](manual_tecnico.pdf) 
* **Manual de Usuario:** [Ver Manual de Usuario (PDF)](manual_usuario.pdf)

---

## 💭 Reflexión personal
### ¿Qué aprendí con este proyecto?
Aprendí a estructurar un programa **modular** aplicando funciones y estructuras de datos como listas, pilas y colas.

También comprendí la importancia de planificar el **pseudocódigo** antes de codificar y de validar cada entrada para evitar errores en la ejecución.

### ¿Qué fue lo más desafiante?
El mayor reto fue integrar los algoritmos de **ordenamiento y búsqueda** de forma que funcionaran correctamente dentro del menú, sin usar librerías externas.

Además, lograr que las estructuras de **pila y cola** se comportaran como en teoría, pero dentro de una lista en Python.

### ¿Qué mejoraría si tuviera más tiempo?
Me gustaría agregar **almacenamiento persistente** (guardado de datos en archivos `.txt` o `.csv`) y un sistema de reportes automáticos.

También implementaría una versión con **interfaz gráfica simple** para mejorar la experiencia del usuario.

---

## 👨‍💻 Autor
Joshua JC

Proyecto final de Programación – 2025

**Repositorio oficial:** [https://github.com/jtepetz/Gestor-de-notas](https://github.com/jtepetz/Gestor-de-notas)
