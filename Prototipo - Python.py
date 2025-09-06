# MÓDULOS

def leerNotaEnRango(min_val, max_val):
    # PRE: min_val <= max_val
    # POST: retorna una nota en el rango [min_val..max_val]
    nota = -1
    while nota < min_val or nota > max_val:
        try:
            nota = float(input(f"Ingrese nota en el rango [{min_val}..{max_val}]: "))
        except ValueError:
            print("Error: debe ingresar un número válido.")
            nota = -1
    return nota

def promedioDeNotas(n1, n2, n3):
    # PRE: cada nota en [0..100]
    # POST: retorna el promedio (n1+n2+n3)/3
    return (n1 + n2 + n3) / 3

def estaAprobado(prom):
    # PRE: prom calculado correctamente
    # POST: retorna True si prom >= 60, False en caso contrario 
    return prom >= 60

def promedioGeneral(sumaPromedios, cantidad):
    # PRE: cantidad > 0
    # POST: retorna sumaPromedios/cantidad
    return sumaPromedios / cantidad

def mostrarResumen(promedios, estados, N, promedioG, totalA, totalR):
    # PRE: promedios calculados y estados determinados
    # POST: muestra el resumen general en pantalla 
    print("--------------- RESUMEN ---------------")
    for i in range(N):
        print(f"Estudiante {i+1}: Promedio = {promedios[i]:.2f} Estado = {estados[i]}")
    print(f"Promedio general del grupo: {promedioG:.2f}")
    print(f"Total de aprobados: {totalA}")
    print(f"Total de reprobados: {totalR}")

# PROGRAMA PRINCIPAL

def main():
    # Entrada
    N = int(input("Ingrese la cantidad de estudiantes: "))

    # Inicializaciones
    sumaPromedios = 0
    totalA = 0
    totalR = 0
    promedios = []
    estados = []

    # Procesamiento
    for i in range(N):
        print(f"\n=== Estudiante {i+1} ===")
        n1 = leerNotaEnRango(0, 100)
        n2 = leerNotaEnRango(0, 100)
        n3 = leerNotaEnRango(0, 100)

        prom = promedioDeNotas(n1, n2, n3)
        promedios.append(prom)

        if estaAprobado(prom):
            estados.append("Aprobado")
            totalA += 1
        else:
            estados.append("Reprobado")
            totalR += 1

        sumaPromedios += prom

    promedioG = promedioGeneral(sumaPromedios, N)

    # Salida
    mostrarResumen(promedios, estados, N, promedioG, totalA, totalR)


if __name__ == "__main__":
    main()
