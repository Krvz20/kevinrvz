#ejercicio 3
""" Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. 
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja 
de todo el grupo. """

# Inicializar variables
sumaCalificaciones = 0
calificacionMaxima = 0
calificacionMinima = 999
# Leer las calificaciones de 5 alumnos
for i in range(5):
 calificacion = int(input("Ingrese la calificación del alumno: "))
 sumaCalificaciones += calificacion
 if calificacion > calificacionMaxima:
    calificacionMaxima = calificacion
 if calificacion < calificacionMinima:
    calificacionMinima = calificacion
# Calcular el promedio
promedio = sumaCalificaciones / 5
# Imprimir resultados
print(f"El promedio de las calificaciones es: {promedio}")
print(f"La calificación más alta es: {calificacionMaxima}")