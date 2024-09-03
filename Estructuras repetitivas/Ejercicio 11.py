#ejercicio 11
""" Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa 
se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio 
,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos 
que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad 
sea igual a 0."""

# Inicialización de variables para contadores y acumuladores
contador_hombres = 0
contador_mujeres = 0
suma_alturas = 0
contador_altura_mayor_170 = 0
contador_altura_menor_150 = 0
contador_alumnos = 0

while True:
    # Solicitar datos del alumno
    print("\nIngrese los datos del alumno:")
    edad = int(input("Edad (Ingrese 0 para terminar): "))
    
    # Verificar si se debe terminar el programa
    if edad == 0:
        break
    
    sexo = input("Sexo (H para hombre, M para mujer): ").strip().upper()
    altura = float(input("Altura (en cm): "))
    
    # Contar cantidad de hombres y mujeres
    if sexo == 'H':
        contador_hombres += 1
    elif sexo == 'M':
        contador_mujeres += 1
    else:
        print("Sexo no válido. Ingrese 'H' para hombre o 'M' para mujer.")
        continue  # Volver a pedir datos si el sexo es inválido
    
    # Acumulación de altura para calcular el promedio
    suma_alturas += altura
    contador_alumnos += 1
    
    # Contar alumnos según su altura
    if altura > 170:
        contador_altura_mayor_170 += 1
    if altura <= 150:
        contador_altura_menor_150 += 1

# Calcular la altura promedio
def calcular_promedio(suma, contador):
    if contador == 0:
        return 0
    return suma / contador

# Mostrar resultados
print("\nResumen de datos")