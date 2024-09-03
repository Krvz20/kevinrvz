#ejercicio 4
""" Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se 
digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto. """

# Solicitar al usuario que ingrese un número para calcular su tabla de multiplicar
numero = int(input("Ingrese un número para calcular su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar del número ingresado
print(f"\nTabla de multiplicar del {numero}:")

# Iterar del 1 al 10 para generar la tabla de multiplicar
for multiplicador in range(1, 11):
    producto = numero * multiplicador
    print(f"{numero} x {multiplicador} = {producto}")