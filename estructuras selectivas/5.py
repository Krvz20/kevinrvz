#ejercicio 5
# Solicita al usuario que ingrese su género y convierte la entrada a minúsculas
genero = input("¿Cuál es su genero, Masculino o Femenino?: ").lower()
# Solicita al usuario que ingrese su edad y la convierte a tipo entero
edad = int(input("Introduzca su edad: "))
# Verifica si el género ingresado es válido
if genero not in "masculino" or "femenino":
    # Muestra un mensaje de error si el género no es 'masculino' ni 'femenino'
    print("Entrada inválida. Por favor, ingrese 'Masculino' o 'Femenino'.")
    exit  # Finaliza el programa si la entrada es inválida
# Verifica si la edad ingresada es negativa
elif edad <= 0:
    # Muestra un mensaje de error si la edad es igual o menor a 0
    print("Entrada inválida. Por favor, ingrese un número positivo (mayor que 0).")
    exit  # Finaliza el programa si la entrada es inválida
# Si el género es 'masculino', calcula las pulsaciones para hombres
elif genero == "masculino":
    # Calcula las pulsaciones por minuto para un hombre basado en la fórmula (210 - edad) / 10
    pulsacionesHombre = (210 - edad) / 10
    # Imprime el resultado indicando el género, la edad y las pulsaciones
    print(f"Usted es género {genero} y tiene {edad} años, por lo cual usted tiene {pulsacionesHombre} pulsaciones al hacer aeróbicos cada 10s")
# Si el género no es 'masculino', se asume que es 'femenino'
else:
    # Calcula las pulsaciones por minuto para una mujer basado en la fórmula (220 - edad) / 10
    pulsacionesMujer = (220 - edad) / 10
    # Imprime el resultado indicando el género, la edad y las pulsaciones
    print(f"Usted es género {genero} y tiene {edad} años, por lo cual usted tiene {pulsacionesMujer} pulsaciones al hacer aeróbicos cada 10s")