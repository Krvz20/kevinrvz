#ejercicio 7
# Solicita al usuario la cantidad de llantas 'Todo Terreno' que va a comprar y convierte la entrada a entero
cantidadProductos = int(input("Ingrese la cantidad de llantas 'Todo Terreno' que va a comprar: "))
# Verifica si la cantidad ingresada es negativa, en cuyo caso muestra un mensaje de error
if cantidadProductos < 0:
    print("Entrada inválida. Por favor, ingrese un número positivo (mayor que 0).")
# Si la cantidad es menor a 5, aplica el precio estándar
elif cantidadProductos < 5:
    precio = 300000  # Precio por llanta si se compran menos de 5
    total = precio * cantidadProductos  # Calcula el costo total
# Si la cantidad está entre 5 y 10 (inclusive), aplica el descuento
elif cantidadProductos >= 5 and cantidadProductos <= 10:
    precio = 250000  # Precio por llanta si se compran entre 5 y 10
    total = precio * cantidadProductos  # Calcula el costo total
# Si la cantidad es mayor a 10, aplica un precio más bajo
else:
    precio = 200000  # Precio por llanta si se compran más de 10
    total = precio * cantidadProductos  # Calcula el costo total
# Imprime el precio por llanta y el total a pagar
print(f"Por cada llanta deberá pagar ${precio}, siendo así un total de: ${total}")