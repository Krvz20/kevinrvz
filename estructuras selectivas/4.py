#ejercicio 4
import random  # Importa el módulo random para generar elecciones aleatorias
# Lista de colores disponibles para la elección
colores = ["rojo", "verde", "azul", "amarillo", "negro", "blanco"]
# Selecciona aleatoriamente un color de la lista
choiceColor = random.choice(colores)
# Imprime el color elegido
print(f"El color elegido fue {choiceColor}")
# Solicita al usuario el valor total de la compra y lo convierte a tipo entero
totalCompra = int(input("Ingrese el valor total de la compra: "))
# Verifica el color elegido para aplicar el descuento correspondiente
if choiceColor == "rojo":
    # Calcula el descuento del 15% si el color elegido es rojo
    descuento = totalCompra * (15 / 100)
    # Calcula el total a pagar después de aplicar el descuento
    final = totalCompra - descuento
elif choiceColor == "verde":
    # Calcula el descuento del 20% si el color elegido es verde
    descuento = totalCompra * (20 / 100)
    # Calcula el total a pagar después de aplicar el descuento
    final = totalCompra - descuento
else:
    # Si el color elegido no es ni rojo ni verde, no se aplica descuento
    descuento = 0
    final = totalCompra
    # Imprime un mensaje indicando que el color elegido no tiene descuento
    print(f"Los colores con descuento son verde y rojo. Su color fue {choiceColor}, por lo cual no accede a un descuento a su compra.")
# Imprime el valor total de la compra, el color elegido, el descuento aplicado y el total a pagar
print(f"El valor total de su compra es: {totalCompra}, El color elegido fue: {choiceColor}, el descuento es de: {descuento}, y el total a pagar es de: {final}.")