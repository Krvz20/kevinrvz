#ejercicio1
# Contadores para los números positivos, negativos y neutros
numeroPositivo = 0
numeroNegativo = 0
numeroNeutral = 0
# Se leen 20 números
for i in range(20):
    # Se leen los número desde la entrada del usuario
    Numero = int(input("Ingrese un número: "))
    # define si el número es positivo, negativo o neutro
    if Numero > 0:
        numeroPositivo += 1
    elif Numero < 0:
        numeroNegativo += 1
    else:
        numeroNeutral += 1
# Se imprimen los resultados
print("Cantidad de números positivos:", numeroPositivo)
print("Cantidad de números negativos:", numeroNegativo)
print("Cantidad de números neutros:", numeroNeutral)