#ejercicio 8
""".un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un 
algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e 
imprima""" 

# Inicialización de contadores para cada rango de calificación
contador_menor_50 = 0
contador_50_a_69 = 0
contador_70_a_79 = 0
contador_80_o_mas = 0

# Número total de estudiantes
num_estudiantes = 23

# Recopilar calificaciones de cada estudiante
for i in range(num_estudiantes):
    while True:
        try:
            calificacion = int(input(f"Ingresa la calificación del estudiante {i + 1} (1-100): "))
            if 1 <= calificacion <= 100:
                break
            else:
                print("Calificación no válida. Debe estar entre 1 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

    # Clasificar la calificación y actualizar el contador correspondiente
    if calificacion < 50:
        contador_menor_50 += 1
    elif 50 <= calificacion < 70:
        contador_50_a_69 += 1
    elif 70 <= calificacion < 80:
        contador_70_a_79 += 1
    elif calificacion >= 80:
        contador_80_o_mas += 1

# Mostrar los resultados
print("\nResumen de calificaciones:")
print(f"Cantidad de estudiantes con calificación menor a 50: {contador_menor_50}")
print(f"Cantidad de estudiantes con calificación de 50 o más pero menor que 70: {contador_50_a_69}")
print(f"Cantidad de estudiantes con calificación de 70 o más pero menor que 80: {contador_70_a_79}")
print(f"Cantidad de estudiantes con calificación de 80 o más: {contador_80_o_mas}")