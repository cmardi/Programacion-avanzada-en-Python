            #-----CARLOS MAMANI-----#
# CONSTRUCCIÓN DE CLASES Y HERENCIA MÚLTIPLE 
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        print(f"{self.nombre} está caminando.")


class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def movimiento(self):
        print(f"{self.nombre} está trotando.")


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def movimiento(self):
        print(f"{self.nombre} está rodando.")


persona = Persona("Carlos")
maratonista = Maratonista("Diego")
ciclista = Ciclista("Francisco")

persona.movimiento()
maratonista.movimiento()
ciclista.movimiento()


