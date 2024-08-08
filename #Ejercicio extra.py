#Ejercicio extra
Nombre_estudiante=str(input("Ingrese el nombre del estudiante: "))
promedioNotas=float(input("Ingrese sus casificaciones: "))
proyecto=float(input("Ingresa tu calificacion de proyecto: "))
parciales = float(input('Ingresa la nota de parcialas: '))

p1 = promedioNotas * 0.3
p2 = proyecto * 0.5
p3 = parciales * 0.2
suma = p1 + p2 + p3

print(f"El estudiante" ,Nombre_estudiante, "tiene una nota final de" ,suma)