#ejercicio 10
""" Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo:"""

# Inicializar el producto en 1
producto = 1

# Crear una lista para almacenar los números y el resultado final
numeros = []

# Multiplicar los números del 1 al 20
for i in range(1, 21):
    producto *= i
    numeros.append(str(i))  # Convertir el número a cadena y agregarlo a la lista

# Crear la cadena de la operación
operacion = ' * '.join(numeros)

# Mostrar el resultado
print(f"El producto de los primeros 20 números naturales es: {operacion} = {producto}")