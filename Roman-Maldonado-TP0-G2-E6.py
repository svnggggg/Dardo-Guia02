class Persona():
    def __init__(self, nombre, edad, vida) -> None:
        self.nombre = nombre
        self.edad = edad
        self.vida = vida

    def mostrarAtributos(self):
        print('- Nombre:', self.nombre)
        print('- Edad:', self.edad)
        print('- Vida:', self.vida)

titoCalderon = Persona('Tito Calderon', 80, 100)
titoCalderon.mostrarAtributos()