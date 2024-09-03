#ejercicio 5
"""Una persona debe realizar un muestreo con 50 personas para determinar el 
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona. 
Las categorías se determinar de acuerdo a la siguiente tabla: """

# Inicialización de variables para almacenar los pesos y los contadores de cada categoría
peso_total_ninos = 0
peso_total_jovenes = 0
peso_total_adultos = 0
peso_total_ancianos = 0

contador_ninos = 0
contador_jovenes = 0
contador_adultos = 0
contador_ancianos = 0

# Número total de personas a ingresar
num_personas = 50

# Recopilar datos de 50 personas
for i in range(num_personas):
    print(f"\nPersona {i + 1}:")
    edad = int(input("Ingrese la edad: "))
    peso = float(input("Ingrese el peso (en kg): "))

    # Clasificar según la edad y acumular el peso y el contador correspondiente
    if 0 <= edad <= 12:
        peso_total_ninos += peso
        contador_ninos += 1
    elif 13 <= edad <= 29:
        peso_total_jovenes += peso
        contador_jovenes += 1
    elif 30 <= edad <= 59:
        peso_total_adultos += peso
        contador_adultos += 1
    elif edad >= 60:
        peso_total_ancianos += peso
        contador_ancianos += 1
    else:
        print("Edad no válida.")

# Calcular y mostrar el promedio de peso para cada categoría
def calcular_promedio(peso_total, contador):
    if contador == 0:
        return 0
    return peso_total / contador

print("\nPromedios de peso por categoría:")
print(f"Niños (0-12 años): {calcular_promedio(peso_total_ninos, contador_ninos):.2f} kg")
print(f"Jóvenes (13-29 años): {calcular_promedio(peso_total_jovenes, contador_jovenes):.2f} kg")
print(f"Adultos (30-59 años): {calcular_promedio(peso_total_adultos, contador_adultos):.2f} kg")
print(f"Ancianos (60 años en adelante): {calcular_promedio(peso_total_ancianos, contador_ancianos):.2f} kg")