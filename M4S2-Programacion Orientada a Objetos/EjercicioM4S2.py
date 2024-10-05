        #-----CARLOS MAMANI-----#
# CLASE ANIMAL Y REPRESENTACIÓN DE OBJETOS E INSTANCIAS #
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        # Inicializa los atributos de la clase Animal
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    # Retorna una representación en forma de cadena del objeto Animal, hace que se visualice mejor al momento de imprimir
    def __str__(self):
        return f"{self.nombre} es un {self.raza} de {self.edad} y pesa {self.peso}"
# Instansiación de la clase Animal        
caballo = Animal("Zeus", "Pura sangre", "5 años", "450 kg.")
leon = Animal("Boulder", "Atlas", "10 años", "130 kg.")

# Imprime las representaciones de los animales
print(caballo)
print(leon)