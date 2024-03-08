class Libro():
    def __init__(self, nombre, autor, hojas, tamaño) -> None:
        self.nombre = nombre
        self.autor = autor
        self.hojas = hojas
        self.tamaño = tamaño

    def mostrarAtributos(self):
        print('# Nombre del libro:', self.nombre)
        print('- Autor del libro:', self.autor)
        print('- Cantidad de hojas:', self.hojas)
        print('- Tamaño del libro:', self.tamaño,'(en cm)')

    def cambiarDatos(self):
        print('Posta queres cambiar los datos del libro??, cambialos!')
        self.nombre = input('Ingresa un nombre: ')
        self.autor = input('Ingresa un autor: ')
        self.hojas = int(input('Ingresa una cantidad de hojas: '))
        self.tamaño = input('Ingresa un tamaño: ')

libro1 = Libro('La increible vida del duko', 'Duko', 200, 70)

libro1.mostrarAtributos()
libro1.cambiarDatos()
libro1.mostrarAtributos()