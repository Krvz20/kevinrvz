#ejercicio2
# Inicializar una variable para almacenar la suma de los números convertidos
numeroPositivossumados = 0
# Leer 10 números negativos del usuario
for i in range(10):
    # se leen los número desde la entrada del usuario
    Numero = int(input("Ingrese un número negativo: "))
    # Verificar si el número es negativo
    if Numero < 0:
        # Convertir el número a positivo
        numeroPositivo = -Numero
        # Sumar el número positivo a la suma total
        numeroPositivossumados += numeroPositivo
    else:
        # Si el número ingresado no es negativo, mostrar un mensaje de error
        print("El número ingresado no es negativo. Por favor, ingrese un número negativo.")
# Imprimir la suma de los números positivos
print(f'La suma de los números convertidos a positivos es: {numeroPositivossumados}')