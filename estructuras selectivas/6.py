#ejercicio 6
# Solicita al usuario que ingrese su nota promedio y la convierte a tipo float
promedioNota = float(input("Por favor coloque su nota promedio: "))
# Solicita al usuario que ingrese la cifra de la pensión a pagar y la convierte a tipo int
pensionAlumno = int(input("Inserte la cifra de la pensión a pagar: "))
# Verifica si el promedio de la nota es igual o mayor a 4
if promedioNota >= 4:
    # Calcula el descuento del 30% sobre la pensión
    descuento = pensionAlumno * (30 / 100)
    # Calcula el total a pagar después de aplicar el descuento
    total = pensionAlumno - descuento
    # Imprime el total a pagar y el monto del descuento aplicado
    print(f"El alumno deberá pagar {total} de pensión, esto gracias al descuento asignado por su nota. El descuento es de {descuento}.")
else:
    # Calcula el aumento del 10% sobre la pensión si no se alcanza la nota mínima
    descuento = pensionAlumno * (10 / 100)
    # Calcula el total a pagar después de aplicar el incremento
    total = pensionAlumno + descuento
    # Imprime el total a pagar y el incremento aplicado
    print(f"Lamentamos que no haya logrado superar la nota mínima para el descuento de pensión. Como resultado pagará un total de ${total} en pensión e IVA.")