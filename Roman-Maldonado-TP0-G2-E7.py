class Banco():
    def __init__(self, nombre, dinero, caja) -> None:
        self.nombre = nombre
        self.dinero = dinero
        self.caja = caja
    
    def datosBanco(self):
        print('# Datos de:', self.nombre)
        print('- Dinero en mano: $', self.dinero)
        print('- Dinero alguna vez depositado: $', self.caja)

    def depositar(self):
        valor = (float(input('# Cuanto desea depositar en la caja de ahorros?: ')))
        if valor < 0:
            print('- Necesitaras depositar mas!')
        elif valor > self.dinero:
            print('- Flaco, no podes deporistar eso, si ni lo tenes!')
        else: 
            self.dinero = self.dinero - valor
            self.caja = self.caja + valor
            print('- El dinero de la caja de ahorros de', self.nombre, 'es:$',self.caja)
    
    def retirar(self):
        valor2 = (float(input('# Cuanto dinero deseas retirar?: ')))
        if valor2 > self.caja:
            print('- No podes retirar eso porque en la caja hay: $',self.caja)
        else:
            self.caja = self.caja - valor2
            self.dinero = self.dinero + valor2
            print('- Tu dinero en mano es: $', self.dinero)
            print('- Tu dinero en la caja de ahorros es: $', self.caja)

Splinter = Banco('Splinter', 1000, 100)
Splinter.datosBanco()
Splinter.depositar()
Splinter.retirar()