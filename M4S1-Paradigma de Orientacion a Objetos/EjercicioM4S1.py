            #-----CARLOS MAMANI-----#
#DISEÑO DE LA CLASE ANIMAL Y REPRESENTACIÓN DE OBJETOS DE INSTANCIAS

class Animal:
    def __init__(self, nombre, raza, edad, peso):   # Inicializa los atributos de la clase Animal
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def comer(self):
        return f"{self.nombre} está comiendo"   # Método que simula que el animal está comiendo

    def caminar(self):
        return f"{self.nombre} está caminando"  # Método que simula que el animal está caminando

    def dormir(self):
        return f"{self.nombre} está durmiendo"  # Método que simula que el animal está durmiendo

# Instansiación de la clase Animal 
perro = Animal("Brando", "San Bernardo", "3 Años", "30 kg.")    # Instancia de un perro
gato = Animal("Roll", "Persa", "4 Años", "3 kg.")               # Instancia de un gato

# Imprime los atributos del perro
print(f"Nombre: " +perro.nombre)
print(f"Raza: " +perro.raza)
print(f"Edad: " +perro.edad)
print(f"Peso: " +perro.peso)
print() # Línea en blanco para separar la salida

# Llama a los métodos del perro e imprime sus acciones
print(perro.comer())
print(perro.caminar())
print(perro.dormir())
print() # Línea en blanco para separar la salida

# Imprime los atributos del gato
print(f"Nombre: " +gato.nombre)
print(f"Raza: " +gato.raza)
print(f"Edad: " +gato.edad)
print(f"Peso: " +gato.peso)
print()

# Llama a los métodos del gato e imprime sus acciones
print(gato.comer())
print(gato.caminar())
print(gato.dormir())
