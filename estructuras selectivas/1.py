#Ejercicio 1
Nombre=input("Digite el nombre del estudiante: ")
Nota1=int(input("Dijite su primera nota: "))
Nota2=int(input("Dijite su segunda nota: "))
Nota3=int(input("Dijite su tercera nota: "))
Promedio= (Nota1 + Nota2 + Nota3) / 3
if Promedio>=70:
  print (f"El estudiante" ,Nombre, "aprueba")
elif Promedio<70:
  print(f"el estudiante" ,Nombre, "no aprueba ") 
else:
  print(f"no dijito bien sus notas") 