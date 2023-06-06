# Actividad 1: 
# Diseña una aplicación que pida por consola una ciudad de destino. 
# Si introduces un 0 y pulsas intro, sales de la aplicación. (5 puntos).
# Si introduces madrid, sevilla o valencia, te permite continuar y te pregunta cuántas
# noches de hotel necesitas. 
# Es indiferente que escribas las ciudades en mayúsculas o minúsculas... (10 puntos)
# Al escribir las noches de hotel te muestra un error si no introduces un número. (5 puntos)
# Una vez finalizado, te muestra un mensaje indicando la ciudad y las noches de hotel que has introducido. (5 puntos)

import time

def actividad1():
    try:
        ciudad = input('Introduce una ciudad de destino: ')

        if ciudad.lower() == '0': # Si la ciudad es 0, sale de la aplicación
            print('Saliendo de la aplicación...')
            time.sleep(1) # Espera 1 segundo antes de salir
            print('Has salido de la aplicación')

        elif ciudad.lower() == 'madrid' or ciudad.lower() == 'sevilla' or ciudad.lower() == 'valencia': # Si la ciudad es Madrid, Sevilla o Valencia, te permite continuar
            noches = input('Introduce las noches de hotel: ')

            if noches.isdigit(): # Comprueba si es un número entero
                time.sleep(0.5) # Espera medio segundo antes de mostrar el mensaje
                print(f'Has elegido {ciudad.title()} y {noches} noches de hotel') # Muestra el mensaje con la ciudad (con la primera letra en mayúsculas) y las noches de hotel elegidas
            else:
                print('No has introducido un número')

        else:
            print('!ERROR¡ No has introducido una ciudad válida')

    except: # Si se produce un error, muestra el mensaje
        print('Ha ocurrido un error inesperado, vuelve a intentarlo')

    finally: # Cuando acaba el programa, muestra el mensaje
        print('\nFin del programa. ¡Hasta pronto!')

actividad1()