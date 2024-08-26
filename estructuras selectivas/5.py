#ejercicio 5
Nombre = input ('Ingrese su nombre: ')
sexo = input ('Ingrese el sexo: ')
edad = int(input('Ingrese la edad: '))


if sexo == 'femenino':
        pulsaciones = 0
        pulsaciones = (220 - edad) /10
        print(f'Señor@ {Nombre}, su numero de pulsaciones por cada 10 segundos de ejercicio: {pulsaciones: .2f}')
elif sexo == 'masculino':
        pulsaciones = 0 
        pulsaciones = (210 - edad) /10
        print(f'Señor@ {Nombre}, su numero de pulsaciones por cada 10 segundos de ejercicio: {pulsaciones: .2f}')
else: 
        print('sexo no reconocido. usar femenino o masculino')