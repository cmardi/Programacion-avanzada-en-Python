class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def comer(self):
        return f"{self.nombre} está comiendo"

    def caminar(self):
        return f"{self.nombre} está caminando"

    def dormir(self):
        return f"{self.nombre} está durmiendo"

  
perro = Animal("Brando", "San Bernardo", "3 Años", "30 kg.")
gato = Animal("Roll", "Persa", "4 Años", "3 kg.")

print(f"Nombre: " +perro.nombre)
print(f"Raza: " +perro.raza)
print(f"Edad: " +perro.edad)
print(f"Peso: " +perro.peso)
print()
print(perro.comer())
print(perro.caminar())
print(perro.dormir())
print()
print(f"Nombre: " +gato.nombre)
print(f"Raza: " +gato.raza)
print(f"Edad: " +gato.edad)
print(f"Peso: " +gato.peso)
print()
print(gato.comer())
print(gato.caminar())
print(gato.dormir())
