# Actividad 2: 
# Diseña las clases Rectangulo, Cuadrado y Pentágono. Estas clases tienen el nombre del polígono y su número de lados. (10 puntos)
# Diseña una aplicación por consola que nos permita introducir el nombre y la longitud para cada tipo de polígono. 
# Te mostrará el nombre y el área del poligono elegio. (10 puntos)
# Utilizas POO y en concreto herencia (5 puntos)

def actividad2():
    try:
        class Poligono: # Clase padre
            def __init__(self, nombre, lados): # Constructor de la clase padre
                self.nombre = nombre
                self.lados = lados

            def mostrarNombre(self): # Método para mostrar los lados
                print(f'Poligono {self.nombre} con {self.lados} lados')

        class Rectangulo(Poligono):
            def __init__(self, nombre, lados, base, altura): # Constructor de la clase hija
                super().__init__(nombre, lados) # Llamo al constructor de la clase padre para que me cree los atributos nombre y lados
                self.base = base
                self.altura = altura

            def area(self): # Método para calcular el área
                print(f'Área: {self.base * self.altura}') # Muestro el área del rectángulo

        class Cuadrado(Poligono):
            def __init__(self, nombre, lados, lado):
                super().__init__(nombre, lados)
                self.lado = lado

            def area(self): # Método para calcular el área del cuadrado
                print(f'Área: {self.lado * self.lado}') # Muestro el área del cuadrado

        class Pentagono(Poligono):
            def __init__(self, nombre, lados, lado):
                super().__init__(nombre, lados)
                self.lado = lado

            def area(self): # Método para calcular el área del pentágono
                print(f'Área: {self.lado * self.lado * 1.72}') # Muestro el área del pentágono

        rectangulo = Rectangulo('rectángulo', 4, 5, 6) # Creo un objeto de la clase Rectangulo
        rectangulo.mostrarNombre() # Llamo al método mostrarNombre
        rectangulo.area() # Llamo al método area

        cuadrado = Cuadrado('cuadrado', 4, 5) # Creo un objeto de la clase Cuadrado
        cuadrado.mostrarNombre() # Llamo al método mostrarNombre
        cuadrado.area() # Llamo al método area

        pentagono = Pentagono('pentágono', 5, 5) # Creo un objeto de la clase Pentagono
        pentagono.mostrarNombre() # Llamo al método mostrarNombre
        pentagono.area() # Llamo al método area

    except:
        print('Ha ocurrido un error inesperado, vuelve a intentarlo')

    finally:
        print('\nFin del programa. ¡Hasta pronto!')

actividad2()