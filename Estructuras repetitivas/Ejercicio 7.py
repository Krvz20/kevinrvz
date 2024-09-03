"""La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad 
de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo 
dígito de la placa de cada carro, se puede determinar el color de la calcomanía 
utilizando la siguiente relación:"""

# Inicialización de contadores para cada color de calcomanía
contador_amarilla = 0
contador_rosa = 0
contador_roja = 0
contador_verde = 0
contador_azul = 0

# Solicitar al usuario el número total de autos
num_autos = int(input("Ingrese el número total de autos que entran a Ibagué: "))

# Recopilar información sobre el último dígito de la placa de cada auto
for i in range(num_autos):
    print(f"\nAuto {i + 1}:")
    ultimo_digito = input("Ingrese el último dígito de la placa: ").strip()

    # Validar que el último dígito sea un número entre 0 y 9
    if ultimo_digito.isdigit() and len(ultimo_digito) == 1:
        ultimo_digito = int(ultimo_digito)
        # Clasificar según el último dígito y actualizar el contador correspondiente
        if ultimo_digito in [1, 2]:
            contador_amarilla += 1
        elif ultimo_digito in [3, 4]:
            contador_rosa += 1
        elif ultimo_digito in [5, 6]:
            contador_roja += 1
        elif ultimo_digito in [7, 8]:
            contador_verde += 1
        elif ultimo_digito in [9, 0]:
            contador_azul += 1
    else:
        print("Dígito no válido. Por favor, ingrese un dígito del 0 al 9.")
        # Decrementar el índice para volver a pedir el dígito en caso de entrada inválida
        i -= 1

# Mostrar los resultados
print("\nCantidad de autos por color de calcomanía:")
print(f"Amarilla: {contador_amarilla}")
print(f"Rosa: {contador_rosa}")
print(f"Roja: {contador_roja}")
print(f"Verde: {contador_verde}")
print(f"Azul: {contador_azul}")