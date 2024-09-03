#ejercicio 6
"""Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un 
total de n personas.""" 

# Solicitar al usuario el número total de personas en el salón
num_personas = int(input("Ingrese el número total de personas en el salón: "))

# Inicialización de contadores para hombres y mujeres
contador_hombres = 0
contador_mujeres = 0

# Recopilar información sobre el género de cada persona
for i in range(num_personas):
    print(f"\nPersona {i + 1}:")
    genero = input("Ingrese el género (H para hombre, M para mujer): ").strip().upper()

    # Clasificar según el género ingresado
    if genero == 'H':
        contador_hombres += 1
    elif genero == 'M':
        contador_mujeres += 1
    else:
        print("Género no válido. Por favor, ingrese 'H' para hombre o 'M' para mujer.")
        # Decrementar el índice para volver a pedir el género en caso de entrada inválida
        i -= 1

# Mostrar los resultados
print(f"\nCantidad de hombres: {contador_hombres}")
print(f"Cantidad de mujeres: {contador_mujeres}")
print(f"\nCantidad de hombres: {contador_hombres}")
print(f"Cantidad de mujeres: {contador_mujeres}")