#Ejercicio 3
# Solicita al usuario que ingrese el monto total de la compra y lo convierte a tipo entero
montoTotal = int(input("Ingresa el monto total de la compra: "))
# Verifica si el monto total es mayor o igual a 500,000
if montoTotal >= 500000:
    # Calcula el porcentaje del monto total destinado a stock de la empresa
    stockEmpresa = montoTotal * (55 / 100)
    # Calcula el porcentaje del monto total destinado al préstamo del banco
    prestamoBanco = montoTotal * (30 / 100)
    # Calcula el porcentaje del monto total destinado al crédito del fabricante
    creditoFabricante = montoTotal * (15 / 100)
    # Imprime los valores calculados para stock de la empresa, préstamo del banco y crédito del fabricante
    print(f"Dinero empresa a salir: {stockEmpresa}, Prestamo banco: {prestamoBanco}, Credito Fabricante: {creditoFabricante}")
# Verifica si el monto total es menor o igual a 500,000
elif montoTotal <= 500000:
    # Calcula el porcentaje del monto total destinado a stock de la empresa
    stockEmpresa = montoTotal * (70 / 100)
    # Calcula el porcentaje del monto total destinado al crédito del fabricante
    creditoFabricante = montoTotal * (30 / 100)
    # Calcula los intereses sobre el crédito del fabricante (20% del crédito)
    intereses = creditoFabricante * (20 / 100)
    # Imprime los valores calculados para stock de la empresa, crédito del fabricante y los intereses
    print(f"Dinero empresa a salir: {stockEmpresa}, Credito Fabricante: {creditoFabricante}, Intereses: {intereses}")
# Si el monto total no cumple con ninguna de las condiciones anteriores, muestra un mensaje de error
else:
    print("Vuelve a intentar")