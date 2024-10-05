            #-----CARLOS MAMANI-----#
# DISEÑO DE COMPORTAMIENTO Y SIMULACIÓN PERTENECIENTES A UNA SELECCIÓN DE FUTBOL #

class Persona:
    def __init__(self,id, nombre, apellidos, edad):     # Inicializa los atributos de la clase Persona
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarse():          # Método que simula que la persona se concentra, sin implementar
        pass

    def viajar():               # Método que simula que la persona se viaja, sin implementar
        pass

class Futbolista(Persona):
    # Inicializa los atributos de la clase Futbolista, heredando de la clase Persona
    def __init__(self, id, nombre, apellidos, edad, dorsal , demarcacion):      
        super().__init__(id, nombre, apellidos, edad)   # Llama al constructor de la clase padre e inicializa atributos en común.
        self.dorsal = dorsal                # Número de dorsal del futbolista
        self.demarcacion = demarcacion      # Demarcación o posición del futbolista
    def jugarPartido():
        # Método que simula que el futbolista juega un partido, sin implementar
        pass
    def entrenar():
        # Método que simula que el futbolista entrena, sin implementar
        pass

class Entrenador(Persona):
    # Inicializa los atributos de la clase Entrenador, heredando de la clase Persona
    def __init__(self, id, nombre, apellidos, edad, idFederacion):
        super().__init__(id, nombre, apellidos, edad)   # Llama al constructor de la clase padre e inicializa atributos en común
        self.idFederacion = idFederacion                # Identificación de la federación del entrenador
    def dirigirPartido():
        # Método que simula que el entrenador dirige un partido, sin implementar
        pass
    def dirigirEntrenamiento():
        # Método que simula que el entrenador dirige un entrenamiento, sin implementar
        pass

class Masajista(Persona):
    # Inicializa los atributos de la clase Masajista, heredando de la clase Persona
    def __init__(self, id, nombre, apellidos, edad, titulacion, añosExperiencia):
        super().__init__(id, nombre, apellidos, edad)   # Llama al constructor de la clase padre e inicializa atributos en común
        self.titulacion = titulacion                    # Titulación del masajista
        self.añosExperiencia = añosExperiencia          # Años de experiencia del masajista
    def darMasajes():
        # Método que simula que el masajista da masajes, sin implementar
        pass

    

        