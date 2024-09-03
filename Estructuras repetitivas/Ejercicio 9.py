#ejercicio 9
"""Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos"""

# Inicialización de variables para almacenar la suma de edades y el conteo
suma_edades_hombres = 0
suma_edades_mujeres = 0
suma_edades_total = 0

contador_hombres = 0
contador_mujeres = 0
contador_total = 0

# Solicitar al usuario el número total de alumnos
num_alumnos = int(input("Ingrese el número total de alumnos: "))

# Recopilar información sobre las edades y géneros de cada alumno
for i in range(num_alumnos):
    print(f"\nAlumno {i + 1}:")
    while True:
        try:
            edad = int(input("Ingrese la edad del alumno: "))
            if edad > 0:
                break
            else:
                print("Edad no válida. Debe ser un número positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

    genero = input("Ingrese el género del alumno (H para hombre, M para mujer): ").strip().upper()

    # Clasificar según el género e incrementar los contadores y sumas correspondientes
    if genero == 'H':
        suma_edades_hombres += edad
        contador_hombres += 1
    elif genero == 'M':
        suma_edades_mujeres += edad
        contador_mujeres += 1
    else:
        print("Género no válido. Por favor, ingrese 'H' para hombre o 'M' para mujer.")
        # Decrementar el índice para volver a pedir la información en caso de entrada inválida
        i -= 1
        continue
    
    suma_edades_total += edad
    contador_total += 1

# Calcular los promedios de edad
def calcular_promedio(suma_edades, contador):
    if contador == 0:
        return 0
    return suma_edades / contador

# Imprimir los resultados
print("\nPromedios de edad:")
print(f"Promedio de edad de hombres: {calcular_promedio(suma_edades_hombres, contador_hombres):.2f}")
print(f"Promedio de edad de mujeres: {calcular_promedio(suma_edades_mujeres, contador_mujeres):.2f}")
print(f"Promedio de edad de todo el grupo: {calcular_promedio(suma_edades_total, contador_total):.2f}")