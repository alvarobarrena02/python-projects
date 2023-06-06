# Actividad 4:
# Se inicia la aplicación y se genera un número aletario entre el 1 y el 9 (5 puntos)
# La aplicación nos pide que adivinemos este número aleatorio. 
# Seguirá mostrando el mensaje hasta que hayamos adivinado el número (5 puntos)
# Muestra el total de intentos que has necesitado para adivinar el número. 
# Si has necesitado más de 3 muestra un mensaje indicando que prueba no superada (5 puntos)
# No puedes repetir un número que ya hayas indicado (5 puntos)
# Muestra cuánto tiempo tarda el programa en ejecutarse desde su inicio hasta que
# muestra el mensaje final que el número ha sido adivinado (5 puntos)

import random
import time

def actividad4():
    try:

        numero_aleatorio = random.randint(1, 9) # Genero un número aleatorio entre el 1 y el 9

        intentos = [] # Creo una lista para almacenar los intentos del usuario

        contador_intentos = 0 # Inicio el contador de intentos a 0

        inicio = time.time() # Inicio el contador de tiempo

        while True:
            numero_usuario = input('Introduce un número del 1 al 9: ') # Pido que se introduzca un número del 1 al 9

            # Comprobamos que el valor introducido es un número
            if numero_usuario.isdigit(): # Si el valor introducido es un número entero lo guarda en la variable numero_usuario
                numero_usuario = int(numero_usuario) # Convierto el valor introducido a entero
                contador_intentos += 1 # Incremento el contador de intentos en 1

                if numero_usuario in intentos: # Si el número introducido está en la lista de intentos muestra un mensaje de error
                    print('Ya has introducido este número, prueba con otro diferente')

                else: # Si el número introducido no está en la lista de intentos lo añade
                    intentos.append(numero_usuario)
                    if numero_usuario == numero_aleatorio: # Si el número introducido es igual al número aleatorio muestra un mensaje de que has acertado
                        print(f'¡Felicidades! Has adivinado el número en {contador_intentos} intentos')
                        print(f'El programa ha tardado {time.time() - inicio} segundos en ejecutarse')
                        break # Salgo del bucle

                    elif numero_usuario < numero_aleatorio: # Si el número introducido es menor que el número aleatorio muestra un mensaje de que el número es mayor
                        print('El número es mayor')

                    else: # Si el número introducido es mayor que el número aleatorio muestra un mensaje de que el número es menor
                        print('El número es menor')

            else: # Si el valor introducido no es un número entero muestra un mensaje de error
                print('Debes introducir un número')

            print(f'Intentos: {intentos}\n') # Muestra los intentos realizados

            if contador_intentos >= 3: # Comprobación de que se ha superado el número máximo de intentos
                print('Has superado el número máximo de intentos, inténtalo de nuevo más tarde')
                break

    except:
        print('Ha ocurrido un error inesperado, vuelve a intentarlo')

    finally:
        print('\nFin del programa. ¡Hasta pronto!')


actividad4()