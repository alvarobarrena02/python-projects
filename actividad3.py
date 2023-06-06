# Actividad 3:
# Crea una colección en donde introduces 4 ciudades y madrid... 
# Debes valorar y explicar brevemente qué tipo de colección vas a utilizar en este caso. 
# Las ciudades se mostrarán ordenadas alfabéticamente. (10 puntos)
# Añade una ciudad al final del listado de ciudades anterior. Y elimina madrid (5 puntos)
# Muestra las ciudades en mayúsculas y el número de letras que la forman. (5 puntos)
# Para todas las ciudades reemplaza las a por la e (5 puntos).

def actividad3():
    try:
        ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza'] #Utilizo esta colección porque es una lista y puedo añadir y eliminar elementos de ella

        ciudades.sort() #Ordeno las ciudades alfabéticamente
        print(f'Las ciudades ordenadas alfabéticamente son: {ciudades}')

        ciudades.append('Valladolid') #Añado una ciudad al final del listado
        print(f'Ciudades actualizadas (append): {ciudades}')

        ciudades.remove('Madrid') #Elimino Madrid
        print(f'Ciudades actualizadas (remove): {ciudades}\n')

        for ciudad in ciudades: #Recorro la lista de ciudades
            print(f'{ciudad.upper()} tiene {len(ciudad)} letras') #Muestro las ciudades en mayúsculas y el número de letras que tiene
            print(f"{ciudad.replace('a', 'e')}") #Reemplazo las 'a' por 'e'
            print('---------------------')

    except:
        print('Ha ocurrido un error inesperado, vuelve a intentarlo')

    finally:
        print('\nFin del programa. ¡Hasta pronto!')

actividad3()