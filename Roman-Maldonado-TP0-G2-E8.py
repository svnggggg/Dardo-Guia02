class Persona():
    def __init__(self, nombre, edad, vida) -> None:
        self.nombre = nombre
        self.edad = edad
        self.vida = vida

    def get_Nombre(self):
        return self.nombre 

    def get_Edad(self):
        return self.edad
    
    def get_Vida(self):
        return self.vida

    def set_masvida(self):
        self.vida = self.vida + 100

titoCalderon = Persona('Tito Calderon', 80, 100)
titoCalderon.set_masvida()

print('#',titoCalderon.get_Nombre())
print('-',titoCalderon.get_Edad())
print('-',titoCalderon.get_Vida())






