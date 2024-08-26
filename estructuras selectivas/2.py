#Ejercicio 2
# Solicita al usuario que ingrese la cantidad de productos que va a comprar y convierte la entrada a tipo entero
cantidadProductos = int(input("Ingrese la cantidad de productos que va a comprar: "))

# Solicita al usuario que ingrese el total de la compra y convierte la entrada a tipo entero
totalCompra = int(input("Ingrese el total de la compra: "))

# Verifica si la cantidad de productos es mayor o igual a 3
if cantidadProductos >= 3:
    # Calcula el descuento del 20% sobre el total de la compra si se compran 3 o más productos
    descuento = totalCompra * (20 / 100)
else:
    # Calcula el descuento del 10% sobre el total de la compra si se compran menos de 3 productos
    descuento = totalCompra * (10 / 100)

# Calcula el total a pagar después de aplicar el descuento
final = totalCompra - descuento

# Imprime el valor de la compra, la cantidad de productos, el descuento aplicado y el total a pagar
print(f"El valor de la compra es de: {totalCompra}, compraste {cantidadProductos}, así que tu descuento es un total de: {descuento}, el total a pagar es de {final}.")