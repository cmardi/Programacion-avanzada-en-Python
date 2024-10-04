class Persona:
    def __init__(self,id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentarse():
        pass

    def viajar():
        pass

class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dorsal , demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion
    def jugarPartido():
        pass
    def entrenar():
        pass

class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, idFederacion):
        super().__init__(id, nombre, apellidos, edad)
        self.idFederacion = idFederacion
    def dirigirPartido():
        pass
    def dirigirEntrenamiento():
        pass

class Masajista(Persona):
    def __init__(self, id, nombre, apellidos, edad, titulacion, añosExperiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.añosExperiencia = añosExperiencia
    def darMasajes():
        pass

    

        