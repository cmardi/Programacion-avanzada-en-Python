        #-----Carlos Mamani-----#

# Importando la función tabulate para mostrar tablas
from tabulate import tabulate

class Persona:
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso ):
        # Inicializar los atributos de la clase Persona
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo
        self._edad = edad 
        self._estatura = estatura
        self._peso = peso
    
    # Métodos para fijar los atributos privados
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_apellido(self, apellido):
        self._apellido = apellido
    def set_sexo(self, sexo):
        self._sexo = sexo
    def set_edad(self, edad):
        self._edad = edad
    def set_estatura(self, estatura):
        self._estatura = estatura
    def set_peso(self, peso):
        self._peso = peso
        
    # Métodos para acceder a los atributos privados
    def get_edad(self):
        return self._edad
    def get_apellido(self):
        return self._apellido

    # Método que define como un objeto se convierte en una cadena #
    # def __str__(self):
        # Retorna una representación e forma de cadena del objeto Persona #
    #     return (f"Nombre: {self._nombre} {self._apellido}\n"
    #             f"Sexo: {self._sexo}\n"
    #             f"Edad: {self._edad}\n"
    #             f"Estatura: {self._estatura}\n"
    #             f"Peso: {self._peso}")

    # Método que convierte los atributos en una lista, facilita la visualización de la tabla
    def to_list(self):
        return(self._nombre, self._apellido, self._sexo, self._edad, self._estatura, self._peso)

# Instanciando, se crean objetos para la clase Persona
persona_1 = Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 mts", "68 Kg.")
persona_2 = Persona("Juan", "Camargo", "Masculino", "18 años", "1.8 mts", "75 Kg.\n")

# Imprimir antes de las modificaciones
print("\nAntes de las modificaciones:\n")
print(tabulate([persona_1.to_list(), persona_2.to_list()], headers=["Nombre", "Apellido", "Sexo", "Edad", "Estatura", "Peso"], tablefmt="grid"))
# Impresión sin la tabla #
# print(persona_1)
# print()
# print(persona_2)

persona_1.set_edad("21 años")
persona_2.set_apellido("Santiago")

# Imprimir después de las modificaciones
print("\nDespués de las modificaciones:\n")
print(tabulate([persona_1.to_list(), persona_2.to_list()], headers = ["Nombre", "Apellido", "Sexo", "Edad", "Estatura", "Peso"], tablefmt = "grid"))
# Impresión sin la tabla #
# print()
# print(persona_2)
    