#ejercicio 4
import random
colores= ['verde','rojo','azul','amarillo','negro','blanco']
valor=int(input("Ingrese su valor"))

pcchoice = random.choice(colores)

print(f'La balota sacada es: {pcchoice}')

if pcchoice == 'rojo':
    descuento= valor * 0.15
    valorFinal = valor - descuento
    print (f"El valor del producto es {valor},el color que saco es {pcchoice}, el valor con el descuento es de {valorFinal}")
elif pcchoice == 'verde':
    descuento= valor * 0.20
    valorFi = valor - descuento
    print (f"El valor del producto es {valor}, el color que saco es {pcchoice}, el valor con el descuento es {valorFi}")
else :
    print (f"El color es {pcchoice} por lo tanto no hay descuento")