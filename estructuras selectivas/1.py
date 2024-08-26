#Ejercicio 1
# Solicita al usuario que ingrese el nombre del aprendiz
aprendiz = input("Ingresa el nombre del aprendiz: ")
# Solicita al usuario que ingrese la nota final, y la convierte a un entero
nota = int(input("Ingresa la nota final: "))
# Verifica si la nota es mayor o igual a 70
if nota >= 70:
    # Si la nota es mayor o igual a 70, se imprime un mensaje indicando que el aprendiz aprobó
    print(f"El aprendiz {aprendiz} aprobó.")
else:
    # Si la nota es menor a 70, se imprime un mensaje indicando que el aprendiz NO aprobó
    print(f"El aprendiz {aprendiz} NO aprobó.")