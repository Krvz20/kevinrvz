#Ejercicio 3
Nombre_empresa=input("Ingrese el nombre de la empresa: ")
Cantidad=int(input("ingrese las cantidades de piezas que compro: "))
Monto=float(input("ingrese el valor individual de cada pieza: "))
Total_monto=(Cantidad * Monto)
if Total_monto>=500000:
    Propio_dinero= Total_monto * 0.55
    Prestado= Total_monto * 0.3
    credito= Total_monto *0.15
    print(f"Señor@s {Nombre_empresa}, Total del monto: {Total_monto} el valor invertido de su propio dinero es {Propio_dinero: .1f}, el valor total del prestamo: {Prestado} y el credito solicitado al fabricante es {credito}") 
elif Total_monto<500000:
    pro_di= Total_monto *0.7
    credi=Total_monto *0.3
    Interes= credi *0.2
    final_monto=credi + Interes
print(f"Señor@s {Nombre_empresa}, Total del monto: {Total_monto} el valor invertido de su propio dinero es {pro_di: .1f}, el valor total del credito es: {credi} con los intereses añadidos que son: {Interes}, y el credito final es {final_monto}")